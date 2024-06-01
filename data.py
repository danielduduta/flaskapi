from flask_caching import Cache

cache = Cache()


employees = {}
employees[1] = {"id":1, "name":"Tiger Nixon","salary":320800,"age":61,"profile_image":""}
employees[2] = {"id":2, "name":"Garrett Winters","salary":170750,"age":63,"profile_image":""}
employees[3] = {"id":3, "name":"Ashton Cox","salary":86000,"age":66,"profile_image":""}
employees[4] = {"id":4, "name":"Cedric Kelly","salary":433060,"age":22,"profile_image":""}
employees[5] = {"id":5, "name":"Airi Satou","salary":162700,"age":33,"profile_image":""}
employees[6] = {"id":6, "name":"Brielle Williamson","salary":372000,"age":61,"profile_image":""}
employees[7] = {"id":7, "name":"Herrod Chandler","salary":137500,"age":59,"profile_image":""}
employees[8] = {"id":8, "name":"Rhona Davidson","salary":327900,"age":55,"profile_image":""}
employees[9] = {"id":9, "name":"Colleen Hurst","salary":205500,"age":39,"profile_image":""}
employees[10] = {"id":10, "name":"Sonya Frost","salary":103600,"age":23,"profile_image":""}


EMP_KEYS = ["name", "salary", "age", "profile_image"]