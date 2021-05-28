## Problem #1

The use of pytest is sparse. Problem #1 required variations on the same data, so from my understanding of the use of pytest fixtures may not have been appropriate since it's only beneficial if the test data doesn't change. There is another option where you can zero out all the data in the pytest fixture, but that seems like a solution looking for a problem.


Another more effective approach to regularly modifying data would be the @pytest.mark.parametrize test function, but I just didn't have enough time.