def LCA(root,p,q):
    curr = root

    while curr:
        if (p.val<curr.val and g.val<curr.val):
            curr=curr.left
        if (p.val>curr.val and g.val>curr.val):
            curr=curr.right
        else:
            return curr