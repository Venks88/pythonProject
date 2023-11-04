import copy
class ValidateSubsequence:
    def isValidSubsequence(self, array, sequence):
        a = set(array);
        b = set(sequence);

        if len(a) == 1 and len(b) == 1:
            return True

        dupeArray = copy.deepcopy(array);
        for i in range(0, len(array)):
            if array[i] not in sequence:
                dupeArray.remove(array[i]);
        if dupeArray == array:
            return True;
        if dupeArray == sequence:
            return True;


array = [1, 1, 1, 1]
sequence = [1, 1, 1]
obj = ValidateSubsequence()
obj.isValidSubsequence(array, sequence)
