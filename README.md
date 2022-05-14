# COSC140 homework 5

## Homework feedback

 * How long did you spend on this homework?

 * What did you think about it?  What was good?  What could be improved?

## Feedback

N

One thing that needs some fixing: 
in the index view function, when you sort by age or price, you should be using the `products` object to call the `order_by` method on so that you also do any necessary filtering, rather than calling it on `Product.objects.all()...` since tht will get rid of the filtering that may have happened earlier in the function.

Everything else looked fine.

