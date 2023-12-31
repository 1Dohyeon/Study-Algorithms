# 선택 정렬(Selection Sort) 알고리즘

선택 정렬 알고리즘은 배열을 정렬하는 간단한 알고리즘으로, 정렬되지 않은 부분에서 가장 작은 원소를 선택하여 정렬된 부분의 끝에 추가하는 방식으로 동작합니다. 아래는 주어진 Java 코드에서 사용된 선택 정렬 알고리즘의 원리입니다.

## 알고리즘 원리

1. 주어진 배열의 길이를 구합니다. 이를 변수 `n`에 저장합니다.

2. 바깥쪽 반복문을 통해 정렬을 반복합니다. 바깥쪽 반복문은 배열의 첫 번째 원소부터 배열의 끝에서 두 번째 원소까지 순회합니다.

3. 내부 반복문을 통해 현재 위치부터 배열의 끝까지 원소를 비교하여 가장 작은 원소의 인덱스(`minIndex`)를 찾습니다.

4. `minIndex`와 현재 위치의 원소를 교환합니다. 이를 통해 정렬된 부분의 끝에 최솟값이 추가됩니다.

5. 위 과정을 반복하면서 배열이 정렬됩니다.

## 예제

다음은 주어진 배열 `{5, 2, 9, 3, 4, 6}`을 선택 정렬하는 과정입니다.

1. 처음 배열: `{5, 2, 9, 3, 4, 6}`
2. 첫 번째 원소 `2`를 선택하여 최솟값으로 설정하고, 나머지 원소와 비교하여 가장 작은 값인 `2`를 현재 위치로 옮깁니다. 배열은 `{2, 5, 9, 3, 4, 6}`이 됩니다.
3. 두 번째 원소 `3`을 선택하여 최솟값으로 설정하고, 나머지 원소와 비교하여 가장 작은 값인 `3`을 현재 위치로 옮깁니다. 배열은 `{2, 3, 9, 5, 4, 6}`이 됩니다.
4. 세 번째 원소 `4`를 선택하여 최솟값으로 설정하고, 나머지 원소와 비교하여 가장 작은 값인 `4`을 현재 위치로 옮깁니다. 배열은 `{2, 3, 4, 9, 5, 6}`이 됩니다.
5. 네 번째 원소 `5`를 선택하여 최솟값으로 설정하고, 나머지 원소와 비교하여 가장 작은 값인 `5`를 현재 위치로 옮깁니다. 배열은 `{2, 3, 4, 5, 9, 6}`이 됩니다.
6. 다섯 번째 원소 `6`을 선택하여 최솟값으로 설정하고, 나머지 원소와 비교하여 가장 작은 값인 `6`을 현재 위치로 옮깁니다. 배열은 `{2, 3, 4, 5, 6, 9}`이 됩니다.

이렇게 반복해서 배열이 정렬됩니다.
