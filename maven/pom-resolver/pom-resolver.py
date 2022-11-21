#!/usr/bin/env python3
import requests
import xml.etree.ElementTree as ET
import urllib.request as r2

group_id="com.google.guava"
artifact_id="guava"
version="31.0.1-jre"

base_url = "https://repo1.maven.org/maven2"

def get_pom(group_id, artifact_id, version):
	target_url = construct_url(group_id, artifact_id, version)
	req = requests.get(target_url)
	if req.status_code == 200:
		return req.text
	
def construct_url(group_id, artifact_id, version=None, extension=".pom"):
	group_path = group_id.replace(".","/")
	if version:
		target_url = f"{base_url}/{group_path}/{artifact_id}/{version}/{artifact_id}-{version}{extension}"
	else:
		target_url = f"{base_url}/{group_path}/{artifact_id}/"
	return target_url

def download_jar(group_id, artifact_id, version=None):
	if version:
		jar_url = construct_url(group_id, artifact_id, version, extension=".jar")
		fn = jar_url.split("/")[-1]
		print("downloading jar",jar_url)
		r2.urlretrieve(jar_url, fn)
		
def process_dependencies_element(x):
	for i in x:
		print("===")
		for j in i:
			print(j.tag)
			print(j.text)

def start(group_id, artifact_id, version=None):
	download_jar(group_id, artifact_id, version)
	pom_text = get_pom(group_id, artifact_id, version)
	pom_xml = ET.fromstring(pom_text)
	for i in pom_xml:
		tag_name = i.tag
		if "dependencies" in tag_name:
			process_dependencies_element(i)
	return "OK"

start(group_id, artifact_id, version)
