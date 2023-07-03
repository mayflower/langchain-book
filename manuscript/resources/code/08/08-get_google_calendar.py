fromlangchain.llmsimportOpenAI
fromlangchain.agentsimportinitialize_agent
fromlangchain.agents.agent_toolkitsimportZapierToolkit
fromlangchain.utilities.zapierimportZapierNLAWrapper

llm=OpenAI(temperature=0)
zapier=ZapierNLAWrapper()
toolkit=ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent=initialize_agent(toolkit.get_tools(),llm,
agent="zero-shot-react-descripti\
on",verbose=True)

agent.run("GetmyGoogleCalendarentriesfortomorrow")
