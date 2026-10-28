def test_api_get_request(playwright):
    request=playwright.request.new_context()
    response=request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status==200
    json_data=response.json()
    print (json_data)
    assert json_data["id"]==1
    request.dispose()
    print("test completed successfully.")

def test_api_post_request(playwright):
    request=playwright.request.new_context()
    response=request.post("https://jsonplaceholder.typicode.com/posts", data={"title": "my test", "body": "hello", "userId": 1})
    assert response.status==201
    json_data=response.json()
    print (json_data)
    assert json_data["title"]=="my test"
    assert json_data["body"]=="hello"
    assert json_data["userId"]==1
    request.dispose()
    print("test completed successfully.")