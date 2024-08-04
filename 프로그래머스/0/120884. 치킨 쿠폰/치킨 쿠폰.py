def solution(chicken):
    benefit = 0
    coupons = chicken

    while coupons >= 10:
        service_chicken = coupons // 10
        benefit += service_chicken
        coupons = service_chicken + (coupons % 10)
    
    return benefit
            