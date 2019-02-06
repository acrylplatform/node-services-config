import hashlib
import json
import sys

def get_file_sha265(hashing_file_path: str) -> str:
	"""
	Compare SHA256
	:param source_hash: hash value
	:param hashing_file_path: file
	:return:
	"""
	hash_ = hashlib.sha256()
	with open(hashing_file_path, 'rb') as hashing_file:
		while True:
			data = hashing_file.read(65536)
			if not data:
				break

			hash_.update(data)

	hash_digest = hash_.hexdigest()
	return hash_digest

def main():
	file_name_ids = {
		'miner-config': 'acryl.conf.sample', 
		'node-service-package': 'Acryl-node-services.tar.gz', 
		'node-service-config': 'config.json',
		'executable': 'acryl.jar'
			}
			
	file_hashes = dict.fromkeys(file_name_ids, '')
	for file_id, file_name in file_name_ids.items():
		sha256_value = get_file_sha265(file_name)
		file_hashes[file_id] = sha256_value
	
	with open('versions.json', 'r') as version_file:
		old_data = json.load(version_file)
	
	for hash_file_name, hash_value in file_hashes.items():
		old_data[hash_file_name]["sha256"] = hash_value

	
	with open('versions.json', 'w') as version_file:
		json.dump(old_data, version_file, indent=4)	
		
	return



if __name__ == "__main__":
    sys.exit(main())
