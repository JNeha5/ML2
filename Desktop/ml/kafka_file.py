import tarfile

tgz_path = r"C:\Users\KIIT0001\Downloads\kafka_2.13-4.1.1.tgz"
extract_path = r"C:\Users\KIIT0001\Downloads\kafka_extracted"

with tarfile.open(tgz_path, "r:gz") as tar:
    tar.extractall(path=extract_path)

print("Kafka extracted successfully!")
