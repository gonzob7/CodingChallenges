'''
Problem: Given an array of integers, return indices of the two numbers such
that they add up to a specific target

Restate: I'm going to have a a function that takes in a list of integers,
as well as a target. My job is to find and return the pair of integers
who's sum is the target, correct?

Questions:
- Will the array be sorted?
- Will there be any negative integers?
- Are there duplicates in the array?
- Are the arrays always going to be relatively small?

Assumptions:
- Numbers will always be integers
- Input is sorted
- Return type is array of two values
'''


def twoSum(nums, target):
    for i in range(len(nums)):
        for x in range(i+1, len(nums)):
            sum = nums[i] + nums[x]
            if sum == target:
                return[nums[i],nums[x]]
    return False


'''
Problem: Merge two sorted linked lists and return it as a new list. The new
list should be made by splicing together the nodes of the first two lists.

Restate: I'm going to have two linked lists, and my goal is to combine both
and have them sorted in a new linked list.


Questions:
- Will there be any negative integers?
- Are there duplicates in a specific array?
- Are the arrays always going to be relatively small?

Assumptions:
- Numbers will always be integers
- Return type is array of both initial lists merged together

PSUDOCODE:

1. create node class
2. create method header that takes in 2 ll
3. create head and curr
4. loop through the lists while there is data left
5. check which is greater from both lists and add that to list
6. return
'''


class Node:
  def __init__(self, data = None, next=None):
    self.val = x
    self.next = next

class Solution:
    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
        curr = Node()
        head = curr
        while l1 or l2:
            if l1 and (not l2 or l1.val <= l2.val):
                curr.next = Node(l1.val)
                l1 = l1.next
            else:
                curr.next = Node(l2.val)
                l2 = l2.next
            curr = curr.next
        return head.next



def main():
    print("yo")

if __name__ == '__main__':
    main()
