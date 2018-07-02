/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root != nullptr){
            std::queue<TreeLinkNode *> q;
            std::queue<TreeLinkNode *> temp;
            temp.push(root->right);
            temp.push(root->left);
            
            while (!temp.empty()){
                q.swap(temp);
                TreeLinkNode *n = nullptr;
                while (!q.empty()) {
                    TreeLinkNode *t = q.front();
                    if (t != nullptr){
                        temp.push(t->right);
                        temp.push(t->left);
                    }
                    n = myConnect(t, n);
                    q.pop();
                }
            }
        }
    }
    
    TreeLinkNode* myConnect(TreeLinkNode *node, TreeLinkNode *next) {
        if (node == nullptr) return next;
        node->next = next;
        return node;
    }
    
    // TreeLinkNode* getNextRightMost(TreeLinkNode *node) {
    //     if (node == nullptr) return nullptr;
    //     if (node->right != nullptr) return node->right;
    //     else return node->left;
    // }
};
