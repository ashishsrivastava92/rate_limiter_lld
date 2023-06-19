
REQUIREMENTS - 

- Accept X number of requests in Y timeslots.


Algo -

1. Token bucket
   - Token Bucket with fixed capacity
   - A refiller which add tokens, in every time interval
   - When Requests comes, get a token from bucket and process request.
   - Each user/ identifier entity, will have a Token bucket.
     
2. Leaking bucket
    - Implemented using Queue(with fixed capacity).
    - If queue is full, request is discarded.
    - This gives a constant rate.
    - Helps in max number of concurrent requests.

3. Fixed window counter
    - For each window, a max number of requests is to be served.

4. Sliding window log
    - No fixed timeframe
    - In the log, timestamp is logged.
    - Even if the request is denied, we store timestamp. Use extra memory.

5. Sliding window counter
    - Fixed Window counter + Sliding window log

Implementation - 

    Classes
    - RateLimiter
      -- (IdentifierType, Algorithm)
         SlidingWindowLimiter
         
    - Algorithm
         - Leaky Bucket
         - SlidingWindow
    - IdentifierType
      - UserIdentifier
        -- User
      - IPIdentifier
         -- IP
    - Driver Class
      -- Composition
      -- Rule (dict)
      -- User Identification















