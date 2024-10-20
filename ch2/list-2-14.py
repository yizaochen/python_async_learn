from asyncio import Future

my_future = Future()

print(f"Is the future done? {my_future.done()}")

my_future.set_result("the result")

print(f"Is the future done? {my_future.done()}")
print(f"The result is: {my_future.result()}")