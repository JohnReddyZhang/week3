# Week 3

### Test-Driven Development, Part 2

We let tests determine the design of our production code.

The basic recipe is:

1. Think of a test that would force the app to evolve by one, small step.
2. Write the test.
3. Run the test suite. (The new test should fail).
4. Write the simplest production code necessary to make the test pass.
5. Run the test suite.  If all tests pass, go to step 6; otherwise go to step 4.
6. Go to step 1.

This recipe is often simplified as the "Red-Green-Refactor" cycle.


Also: https://blog.codinghorror.com/the-best-code-is-no-code-at-all/
