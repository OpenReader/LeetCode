/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool find = false;
    
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        if (!root) return NULL;
        
        // left
        TreeNode* l_ret = inorderSuccessor(root->left, p);
        if (l_ret) return l_ret;
        // visit cur
        if (find) return root;
        if (root == p) find = true;
        // right
        TreeNode* r_ret = inorderSuccessor(root->right, p);
        if (r_ret) return r_ret;
        return NULL;
    }
};