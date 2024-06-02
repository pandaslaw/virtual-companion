# Virtual Companion


Your personal assistant who can be your empathic friend, hot romantic partner or a business companion/advisor.
Pick personality/character you need the most today and start chatting right away!

## Project Setup

1. Download Ollama https://ollama.com/download
2. Run just installed locally Ollama
3. In cmd run ``ollama run llama2`` to pull llama2 model
4. Create .env file. Sample configs are in .env.sample file.
5. Based on your needs run one of the following scripts:
   - Run telegram bot to chat in Telegra,
    > ./py-run-bot.cmd  
   - Run fastapi server to call endpoint
    > ./py-run-server.cmd
   - Run streamlit to chat using GUI in browser
    > ./py-run-streamlit.cmd  
