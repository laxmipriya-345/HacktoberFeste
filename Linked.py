# Python program to delete every k-th Node of
# a singly linked list.
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to remove every kth node in the linked list
def delete_k(head, k):
  
    # If list is empty or k is 0, return the head
    if head is None or k <= 0:
        return head

    curr = head
    prev = None

    count = 0

    while curr is not None:
        count += 1

        # If count is a multiple of k, remove current node
        if count % k == 0:
          
            # Bypass the current node
            if prev is not None:
                prev.next = curr.next
            else:
              
                # If removing the head node
                head = curr.next
        else:
          
            # Update previous node pointer only if
            # we do not remove the node
            prev = curr

        curr = curr.next

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    k = 2
    head = delete_k(head, k)
    print_list(head)
