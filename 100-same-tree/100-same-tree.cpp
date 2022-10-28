/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool inorder(TreeNode* p,TreeNode* q)
    {
        bool x,y,z;
        if(p->left && q->left)
            x=inorder(p->left,q->left);
        else if(!p->left && !q->left)
            x=true;
        else
            return false;
        y=(p->val==q->val);
        if(p->right && q->right)
            z=inorder(p->right,q->right);
        else if(!p->right && !q->right)
            z=true;
        else
            return false;
        return (x && y && z);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q)
            return true;
        else if(p && q)
            return inorder(p,q);
        else
            return false;
    }
};