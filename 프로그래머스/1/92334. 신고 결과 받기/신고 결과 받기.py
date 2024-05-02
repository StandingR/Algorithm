def solution(id_list, report, k):
    reported_users = {}  # 각 사용자가 신고당한 유저들의 신고 유저 목록을 저장하는 딕셔너리
    counts = {}  # 각 사용자가 받은 신고 횟수를 저장하는 딕셔너리

    # 신고 기록 처리
    for r in report:
        user_id, reported_id = r.split()
        
        # reported_id가 신고당한 사용자 목록에 없으면 새로운 집합 생성
        if reported_id not in reported_users:
            reported_users[reported_id] = set()
        
        # 신고한 사용자를 집합에 추가
        reported_users[reported_id].add(user_id)
    
    # 정지 조건을 충족하는 사용자 처리
    for reported_id, reporters in reported_users.items():
        if len(reporters) >= k:
            for reporter in reporters:
                counts[reporter] = counts.get(reporter, 0) + 1

    # 결과 생성
    answer = []
    for user_id in id_list:
        answer.append(counts.get(user_id, 0))

    return answer