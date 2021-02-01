/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *ret, *remain;
        ListNode *head = new ListNode(0);
        ret = head;
        int up = 0;
        while (true) {
            int sum = l1->val + l2->val + up;
            if (sum >= 10) up = 1;
            else up = 0;
            ret->next = new ListNode(sum % 10);
            ret = ret->next;
            l1 = l1->next;
            l2 = l2->next;
            if (!l1) {
                remain = l2;
                break;
            }
            if (!l2) {
                remain = l1;
                break;
            }
        }
        // add remain
        while (remain) {
            int sum = remain->val + up;
            if (sum >= 10) up = 1;
            else up = 0;
            ret->next = new ListNode(sum % 10);
            ret = ret->next;
            remain = remain->next;
        }
        // add final
        if (up) ret->next = new ListNode(1);
        return head->next;
    }
};