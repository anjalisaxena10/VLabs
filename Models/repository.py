from Models.Lab import Lab
from Models.Lab import ExperimentQuiz
import json
import random

# The class represents a Mock repository. The actual implementation
# can be changed with a database layer which fetches data from the DB.
class Repository(object):
    def __init__(self):
        self._labsList = []
        self._experimentquizzes = []

        # create mock labs
        lab = Lab(1, "Computer Science")
        self._labsList.append(lab)
        lab = Lab(2, "Physics")
        self._labsList.append(lab)

        # create mock Experiment quizzes, Experiment name, quiz description & question text are added
        # experiments, quizdescription and questiontext are added using arrays.
        experiments = ["DataStructures", "Computer Algo", "System Design", "Workflows", "OOAD", "OOAP", "AI", "Databaes"]
        quizdescription = ["Choose one", "Which is the largest", "Which is the smallest" , "choose the elective"]
        questionText = ["A", "B","C", "D","E", "F","G", "H","I"]
        for labid in range(1, 3):
            for exp in range(1, 3):
                for quizid in range(1, 4):
                    for questionid in range(1, 9):
                        eq = ExperimentQuiz(exp, quizid, questionid, labid)
                        eq._experimentName = experiments[random.randint(0, experiments.__len__()-1)]
                        eq._quizDescription = quizdescription[random.randint(0, quizdescription.__len__()-1)]
                        eq._questionText = questionText[questionid]
                        self._experimentquizzes.append(eq)


    def getAllLabs(self):
        return self.jsonStr(self._labsList)

    def getLab(self, labid=1):
        nums = [x for x in self._labsList if x._labId == labid]
        return self.jsonStr(nums)

    def getExperimentQuizes(self, labid=1):
        nums = [x for x in self._experimentquizzes if x._labId == labid]
        return self.jsonStr(nums)

    def jsonStr(self, obj):
        return json.dumps(obj, default=lambda o: o.__dict__)


# rep = Repository()
# print(rep.getAllLabs())
# print(rep.getExperimentQuizes(1))
# print(rep.getExperimentQuizes(2))
