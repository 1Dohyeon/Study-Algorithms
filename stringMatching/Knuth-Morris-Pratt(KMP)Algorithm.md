[[���丶Ÿ �˰�����]] �� �̿��� ��Ī ����� ����ϴ�. ��Ī�� �������� �� ���ư� ���¸�  �� �迭 ��´�. �̶� ���� ���;� �ϴ� ���ĺ��� ���Դٰ� �����ϰ� �տ� �ߺ��Ǵ� ���� �ֳ� ���� �� �� �̵��Ѵ�.

### KMP �˰����� ����
- `ababaca` ��� ���ڿ��� ã�´ٰ� ����.
- `P[] = [a, b, a, b, a, c, a]`
- `��[]` <- ��Ī�� �������� �� ���ư� ���� ���� ���¸� ����
- ex) `banana`���� �տ� `ana`�� ���λ�, �ڿ� `ana`�� ���̻�. ���λ��� ������ ���̻��� �Ӹ� `a`�� �����ȴ�. �̸� �����ϴ� �����δ�, ���λ�� ���̻��� ũ��� ���ư� �� �ִ� ���¸� �Ǵ��ϱ� �����̴�.
- ���丶Ÿ������ ���ư� ���� ���ٸ� `0`���·� ���ư�����, KMP �˰����򿡼��� ���ư��� �� ��� `���λ�+1` ĭ���� ���ư���. ������ `���λ�` ũ�⸸ŭ�� �����̸� ������, å���� ������ ���� �ٸ���. ������ ��������� �Ʒ� ���ÿ��� �ڼ��� ����.

- `ababaca` ������� `��`�� ����
1) `a`, `m=1`
    -  �̶��� ���´� `1`�� �����Ѵ�.
    - `��`���� ��Ī ���н� �̵��� ���¸� �����ϱ� ������ ���� ù��° ĭ�� ���� ó�� ���� `0`�� ���� ������.(�ε����� 0�������� ���� ���ϰ� 1�� ����)
    - `��[1] = 0`
2) `b`, `m=2`
    - `ab` ����`k`�� `2`�� ������.
    - `b`�� ã�� ���߱⿡ `��`�� `a`�� �ִ� ���·� ���ư��� �Ѵ�.
    - `��[2] = 1(���λ�(0) + 1)`
3) `a`, `m=3`
    - `aba` ���´� `3`
    - `a`�� ã�� ���� ��� `ab`�� ���¿��� ���ư� ����� ã�ƾ��Ѵ�. ���λ�� ���̻簡 ���� �������� ������ ó�� `a`�� �ִ� ������ `1`�� ���ư���.
    - `��[3] = 1(���λ�(0) + 1)`
4) `b`, `m=4`
    - `abab` ���´� `4`
    - `b`�� ã�� ������ ��� `aba`���� `b`�� �������� ���λ� `a`, ���̻� `b`�� ã�� �� �ִ�.
    - `��[4] = 2(���λ�(1) + 1)`
5) `a`, `m=5`
    - `ababa` ���´� `5`
    - `a`�� ã�� ������ ��� `abab`���� ���λ�� ����`ab`, ���̻�� ���� `ab`�̴�.
    - ���� `��[5] = 3(���λ�(2) + 1)`
6) `c`, `m=6`
    - `ababac` ���´� `6`
    - `c`�� ã�� ���� ����� `ababa`���� �߰� `a`�� �����ϴ� ���λ� `aba`, ���̻� `aba`�� ������ �� �� �ִ�.
    - `��[6] = 4(���λ�(3) + 1)`
7) `a`, `m=7`
    - `ababaca` ���´� `7`
    - `a`�� ã�� ���� ����� `ababac`���� ���λ�� ���̻縦 ã�� �� ����.(��Ȥ �տ� `ababa`���� ã���� �ȵǳİ� �ϴµ�, �ǵ� ���ĺ��� �� ���� �Ǿ���Ѵ�. ���� `c`�� �ڿ����� ã�� �� �ְ�, �տ����� ��ã�� ������ ���λ�� ���̻�� ����.)
    - `��[7] = 1(���λ�(0) + 1)`
    - **���ϴ� ���ڿ��� ã�ұ� ������ ã������ �˸���.**
8) `m+1`
    - ���� ���ĺ��� ã�� ���� ����� `ababaca`���� ù`a`�� ��`a`�� ���λ� ���̻��̴�.
    - `��[8(m+1)] = 2(���λ�(1) + 1)`

���������� `��[] = [0, 1, 1, 2, 3, 4, 1, 2]`

���ư� ���� ���� ���� �� �����ϴ� ���� �ڵ�� �Ʒ��� ����.
```
preprocessing(P[ ]) {
	j ��1;
	k ��0; 
    ��[1] �� 0;
	
    while (j �� m) {
		if (k = 0 or P[j] = P[k]) then { j++; k++; ��[j] �� k; } 
        else k �� ��[k];
	}
}
```

---
### KMP �˰������� �����ڵ�
```
KMP(A[ ], P[ ]) {	// n: �迭 A�� ����, m: �迭 P�� ����
	preprocessing(P); 	// ����ð� ��(m)
    i ��1; 				// ���� ���ڿ� ������
	j ��1; 				// ���� ���ڿ� ������
	
    while (i �� n) {
		if (j = 0 or A[i] = P[j]) then { 
        	i++; j++; 
        } else j �� ��[j];
        if (j = m+1) then {
			A[i-m]���� ��Ī�� �Ͼ���� �˸���;
			j �� ��[j];
        }
	}
}
```
����ð� : `��(n)`