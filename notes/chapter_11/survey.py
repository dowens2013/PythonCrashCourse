class AnonymousSurvey:
    """Collect anonymous answers to survey question"""

    def __init__(self, question):
        """Assign initial attributes"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store question response"""
        self.responses.append(new_response)

    def show_results(self):
        """Show results"""
        print("Survey Responses")
        for x in self.responses:
            print(f"- {x}")

