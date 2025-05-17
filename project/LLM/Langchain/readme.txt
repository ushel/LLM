
ConversationBufferMemory = This memory allows for storing of messages and then extracts the messages in a variable

ConversationBufferWindowMemory = This memory keeps a list of the interactions of the conversation over time. It only uses the last k interactions

ConversationTokenBufferMemory = This memory keeps a buffer of recent transactions in memory, and uses token length rather than number of interactions 
                                to determine when to flush interactions.

ConversationSummaryMemory = This memory creates a summary of the conversation over time.

vector data memory = Stores text ( from conversation or elsewhere) in a vector database and retrieves the most relevant block of text

Entity memories = Using a LLM, it remembers details about specific entities.

you can also use multiple memories at one time.

Conversation memory + Entity memory to recall individuals