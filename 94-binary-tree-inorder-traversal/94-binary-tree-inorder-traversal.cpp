class Solution {
private:
    vector<int> ans;
    void inorder(TreeNode* root){
        if(!root) return;
        
        TreeNode* curr = root, *pre;
        while(curr){
            if(!curr->left){
                ans.push_back(curr->val); curr = curr->right;
            }
            else{
                pre = curr->left;
                while(pre->right != NULL and pre->right != curr){
                    pre = pre->right;
                }
                if(pre->right == NULL){
                    pre->right = curr;
                    curr = curr->left;
                }
                else{
                    pre->right = NULL;
                    ans.push_back(curr->val);
                    curr = curr->right;
                }
            }
        }
        return;
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        inorder(root);
        return ans;
    }
};