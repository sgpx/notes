#include <cstdio>
#include <iostream>
#include <vector>

struct Node
{
    Node *parent;
    std::vector<Node *> children;
    int val;
};

Node *depth_first_search(Node *z, int target)
{
    if (z == nullptr)
        return nullptr;
    else if (z->val == target)
        return z;
    std::vector<Node *> nv = z->children;
    auto it = nv.begin();
    while (it != nv.end())
    {
        auto y = *it;
        if (y->val == target)
            return y;
        else
        {
            Node *t = depth_first_search(y, target);
            if (t != nullptr)
            {
                if (

                    t->val == target)
                {
                    return t;
                }
            }
        }
        ++it;
    }
    return NULL;
}

int main()
{
    Node a, b, c, d, e, f;
    a.val = 1;
    b.val = 2;
    c.val = 3;
    a.parent = NULL;
    b.parent = &a;
    c.parent = &a;
    a.children.push_back(&b);
    a.children.push_back(&c);
    d.val = 6;
    e.val = 4;
    f.val = 5;
    b.children.push_back(&d);
    b.children.push_back(&e);
    c.children.push_back(&f);

    Node *found = NULL;
    found = depth_first_search(&a, 6);
    if (found == NULL)
        std::cout << "not found" << std::endl;
    else
        std::cout << found->val << std::endl;
    return 0;
}
