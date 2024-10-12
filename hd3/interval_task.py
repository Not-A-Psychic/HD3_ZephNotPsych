from uagents import Agent, Context
 

master_phrase = "you are a great person with ammicable personality who loves coffee and pizza."
# Create an agent named Alice
alice = Agent(name="Alice", seed=master_phrase)
 
# Define a periodic task for Alice
@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {alice.name}')
 
# Run the agent
if __name__ == "__main__":
    alice.run()