import os
import routeros_api

try:
  con = routeros_api.RouterOsApiPool(
    'router.contoso.com',
    username='admin',
    password='B@dPassword1!',
    use_ssl=True,
    ssl_verify=False,
    plaintext_login=True
  )
  api = con.get_api()
except:
  print("FAILURE")
  os._exit(1)
print("Address,MAC-Address,Hostname,Last-Seen,Expires-After")
dhcp = api.get_resource('/ip/dhcp-server/lease').get()
for rec in dhcp:
  try:
    hostname = rec['host-name']
  except KeyError:
    hostname = ""
  print(f"{rec['address']},{rec['mac-address']},{hostname},{rec['last-seen']},{rec['expires-after']}")
con.disconnect()
os._exit(0)
