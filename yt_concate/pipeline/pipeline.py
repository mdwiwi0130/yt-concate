from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        date = None
        for step in self.steps:
            try:
                date = step.process(date, inputs)
            except StepException as err:
                print('Exception happened : ', err)
                break
