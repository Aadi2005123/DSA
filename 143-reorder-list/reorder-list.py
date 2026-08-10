class Solution(object):
    def reorderList(self, head):
        nodes = []

        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        l = 0
        r = len(nodes) - 1

        while l < r:
            nodes[l].next = nodes[r]
            l += 1

            if l == r:
                break

            nodes[r].next = nodes[l]
            r -= 1

        nodes[l].next = None