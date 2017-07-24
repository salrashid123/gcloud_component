#!/usr/bin/python
from googlecloudsdk.core.util import files
import hashlib

print files.Checksum(algorithm=hashlib.sha256).AddDirectory('components/').HexDigest()
