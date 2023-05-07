{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cefeeba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from sympy.solvers import solve\n",
    "from sympy import symbols\n",
    "from sympy.core import sympify\n",
    "\n",
    "x, y, z = symbols('x y z')\n",
    "\n",
    "# st.header('聯立方程式求解')\n",
    "st.markdown('# 聯立方程式求解')\n",
    "\n",
    "expr1 = st.text_area('請輸入聯立方程式：', 'x+y=11\\nx-y=5\\ny+z=8')\n",
    "\n",
    "if st.button('求解'):\n",
    "    equations_clean=[]\n",
    "    equations = expr1.split('\\n')\n",
    "    if len(equations)>0:\n",
    "        for i in range(len(equations)):\n",
    "            if equations[i] == '':\n",
    "                continue\n",
    "            arr = equations[i].split('=')\n",
    "            if len(arr) == 2:\n",
    "                equations[i] = arr[0] + '-(' + arr[1] + ')'\n",
    "            equations_clean.append(equations[i])\n",
    "        print(equations_clean)\n",
    "    \n",
    "    ans = solve(equations_clean)\n",
    "    print(ans)\n",
    "    st.write(f'結果:{ans}')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
