# Meeting 2 Notes 24/10/22
- Metabase API Guide: https://www.metabase.com/learn/administration/metabase-api
##Work Divided
- Login Session Token
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "person@metabase.com", "password": "fakepassword"}' \
  http://localhost:3000/api/session
```
- Usman: Add Database request
- Hassan: Get Current User Data Request
- Abdullah: Setup Group Permissions
