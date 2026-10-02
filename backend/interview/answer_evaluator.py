class AnswerEvaluator:
    def evaluate(self,question,answer):
        return {"score":min(100,len((answer or "").split())*2),"feedback":"Use a specific example and explain the result."}
