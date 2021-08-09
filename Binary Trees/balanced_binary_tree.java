/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    private Integer maxDepth(TreeNode root){
        if(root==null){
            return 0;
        }

        Integer leftDepth = maxDepth(root.left);
        Integer rightDepth = maxDepth(root.right);

        if (leftDepth == null || rightDepth == null){
            return null;
        }

        if (Math.abs(leftDepth - rightDepth) > 1){
            return null;
        }

        return Math.max(leftDepth, rightDepth) + 1;
    }
    public boolean isBalanced(TreeNode root) {
        return maxDepth(root) != null;
    }
}