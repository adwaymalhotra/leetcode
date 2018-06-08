# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or not head: return head
        L = 0
        
        n = head
        while n.next:
          L += 1
          n = n.next
        L+=1
        tail = n
        
        k = k % L
        if k==0: return head
        
        n = head
        f = L-k
        while f>1:
          n = n.next
          f-=1
        nh = n.next
        n.next = None
        tail.next = head
        
        return nh

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1: return head
        t = ListNode(-1)
        t.next = head
        i = 1
        n = head.next
        h = head
        p = h
        newHead = False
        while n:
            if i%k==0:
                if not newHead:
                    head = h
                    newHead = True
                t = p
                h = n
                if h: n = h.next 
                else: n = None
                p = h
            else:
                x = n
                t.next = n
                p.next = n.next
                n.next = h
                h = n
                n = p.next
            i+=1
        if i%k > 1:
            h = t.next
            p = h
            n = h.next
            
            while n:
                x = n
                t.next = n
                p.next = n.next
                n.next = h
                h = n
                n = p.next
        elif not newHead: head = t.next
                
        return head

    def oddEvenList(self, head):
        if not head or not head.next: return head
        
        oh = head
        eh = head.next
        t1 = oh
        t2 = eh
        
        i = 1
        t = t2.next
        while t:
            if i%2 == 1:
                t1.next = t
                t1 = t1.next
            else:
                t2.next = t
                t2 = t2.next
            t = t.next
            i+=1
        t2.next = None
        t1.next = eh
        return oh

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if k <= 1: return [root]     
        l = 0
        n = root
        while n:
            l+=1
            n=n.next
        if l == 0: return [None for i in range(k)]
        
        indices = [i for i in range(k)]
        ind = 0
        while indices[-1] < l-1:
            for i in xrange(ind%k, k):
                indices[i] += 1
            ind +=1
        
        ans = [None for i in range(k)]
        ans[0] = root
        n = root
        i = 0
        c = 0
        while n.next != None:
            if c==indices[i]:
                t = n.next
                i+=1
                ans[i] = t
                n.next = None
                n = t
            else:
                n = n.next
            c+=1
            
        return ans

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return head
        d = {}
        f = {}
        f[None] = -1
        d[None] = -1
        
        #storing node locations
        i=0
        n = head
        while n:
            d[n] = i
            n = n.next
            i+=1
        
        #storing rand locations
        n = head
        i = 0
        while n:
            r = n.random
            if r: f[n] = d[r]
            else: f[n] = -1
            i+=1
            n = n.next
        
        e ={}
        i = 1
        nh = RandomListNode(head.label)
        e[0] = nh
        n1 = nh
        n = head.next
        while n:
            t = RandomListNode(n.label)
            e[i] = t
            n1.next = t
            n1 = n1.next
            n = n.next
            i+=1
            
        n = head
        n1 = nh
        i = 0
        while n:
            x = f[n]
            if x != -1:
                n1.random = e[x]
            n = n.next
            n1 = n1.next
            i+=1
            
        return nh