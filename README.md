# asgmt-05-python-for-non-stem
Assignment 05: Python for Non-STEM.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為三種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 程式題：以函數/類別宣告答案，函數/類別名稱下的長字串（docstring）會描述測試資料與預期輸出，能夠讓我們充分暸解預期輸入以及預期輸出之間的對應關係，寫作完畢後要記得輸出答案的變數 `return your_answer_variable`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（是非題）在條件敘述的分支結構中，`else` 分支是必要的結構。

```python
answer_01 = None
```

## 02.（單選題）下列哪一個運算不能夠被 Python 評估為條件（布林值）？

1. `"56" in "5566"`
2. `5566 = "5566"`
3. `bool("5566")`
4. `bool(5566)`

```python
answer_02 = None
```

## 03.（程式題）定義函數 `answer_03()` 能夠將輸入 BMI 值所對應的分類以文字輸出。

|BMI|Category|
|---|--------|
|BMI < 18.5|Underweight|
|18.5 <= BMI < 25|Normal weight|
|25 <= BMI  < 30|Overweight|
|BMI >= 30|Obese|

來源：<https://en.wikipedia.org/wiki/Body_mass_index>。

```python
def answer_03(bmi: float) -> str:
    """
    >>> answer_03(32.90) # Zion Williamson, professional basketball player
    'Obese'
    >>> answer_03(26.63) # LeBron James, professional basketball player
    'Overweight'
    >>> answer_03(24.83) # Roger Federer, professional tennis player
    'Normal weight'
    >>> answer_03(17.58) # Suguru Osako, professional marathon runner 
    'Underweight'
    """
```

## 04.（程式題）定義函數 `answer_04()` 能夠將輸入的資料類別以 `str` 輸出。

```python
def answer_04(x) -> str:
    """
    >>> answer_04(0)
    'int'
    >>> answer_04(1.0)
    'float'
    >>> answer_04(False)
    'bool'
    >>> answer_04(True)
    'bool'
    >>> answer_04('5566')
    'str'
    >>> answer_04(None)
    'NoneType'
    """
```

## 05.（程式題）定義函數 `answer_05()` 能夠將輸入 `list` 的中位元素取出（奇數長度取出中間元素、偶數長度取出中間的兩個元素）。

```python
def answer_05(x: list):
    """
    >>> answer_05([2, 3, 5])
    3
    >>> answer_05([2, 3, 5, 7])
    (3, 5)
    >>> answer_05([2, 3, 5, 7, 11])
    5
    >>> answer_05([2, 3, 5, 7, 11, 13])
    (5, 7)
    """
```