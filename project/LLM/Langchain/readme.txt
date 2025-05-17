
ConversationBufferMemory = This memory allows for storing of messages and then extracts the messages in a variable

ConversationBufferWindowMemory = This memory keeps a list of the interactions of the conversation over time. It only uses the last k interactions

ConversationTokenBufferMemory = This memory keeps a buffer of recent transactions in memory, and uses token length rather than number of interactions 
                                to determine when to flush interactions.

ConversationSummaryMemory = This memory creates a summary of the conversation over time.
