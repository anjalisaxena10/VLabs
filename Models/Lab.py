# The class represents a Model representation of the actual database schema.
# The model will change based on our DB schema.

class Lab(object):

    def __init__(self, ids=0, name=""):
        self._labId = ids
        self._labName = name

class ExperimentQuiz(object):

    def __init__(self, experimentid=0, quizid=0, questionid=0, labid=0):
        self._experimentid = experimentid
        self._quizId = quizid
        self._questionId = questionid
        self._labId = labid
        self._experimentName = ""
        self._quizDescription = ""
        self._questionText = ""
        self._questionType = ""

class StudentAnswer(object):

     def __init__(self, studentid=0, quizid=0, experimentid=0):
        self._studentId = studentid
        self._quizId = quizid
        self._experimentId = experimentid
        self._questionId = 0
        self._answerText = ""

class Student(object):

    def __init__(self, studentid=0, studentname=""):
        self._studentid = studentid
        self._studentname = studentname



#experiment = ExperimentQuiz(9, 5, 3)
#experiment._questionText = "What your name"
#print(json.dumps(experiment, default=lambda o: o.__dict__))
