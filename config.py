import urllib3
import certifi

MATCH_LIMIT = 300
# prepare parameters
playerNames = ['17_shou', '4AMGodVzzZ'] #, 'SnakeTC-baolei']
# playerId17_shou = 'account.6694a37350824b4faa9bd582510caa43'

ZONE = 'pc-as'
url = "https://api.pubg.com/shards/%s/players" % (ZONE)
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

headers = {
    "Authorization":
    "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MjUzYzg3MC02MWM0LTAxMzYtNTZmNC01M2I5NzlmYzY3NjciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMwNzE0NDI5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1wZ2FtZSJ9.hTsACgpnjvanxkS4CQA5GG0zeDnoi-ZRyEqyMUxtUNA",
    "Accept":
    "application/vnd.api+json"
}
