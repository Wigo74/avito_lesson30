import csv
import json

ADS = 'ad'
CATEGORY = 'category'
USER = 'user'
LOC = 'location'


def conv_json(csv_file, json_file, model):

    with open(csv_file, encoding = 'utf-8') as csv_file:
        csv_read = csv.DictReader(csv_file)
        # Converting rows into dictionary and adding it to data
        result = []
        for row in csv_read:
            to_add = {'model': model, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']
            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "price" in row:
                row["price"] = int(row["price"])

            to_add['fields'] = row
            result.append(to_add)

    # dumping the data
    with open(json_file, 'w', encoding = 'utf-8') as jf:
        jf.write(json.dumps(result, ensure_ascii=False))


# conv_json(f"{ADS}.csv", f"{ADS}.json", 'ads.ad')
# conv_json(f"{CATEGORY}.csv", f"{CATEGORY}.json", 'ads.category')
conv_json(f"{USER}.csv", f"{USER}.json", 'users.user')
# conv_json(f"{LOC}.csv", f"{LOC}.json", 'users.location')