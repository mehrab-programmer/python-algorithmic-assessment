{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1675b726",
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b = 1, 2\n",
    "fibo = a, b, a+b\n",
    "\n",
    "def even_fibo():\n",
    "    even = 0\n",
    "\n",
    "    while fibo <= 4000000:\n",
    "        if a or b or a+b % 2 == 0:\n",
    "            \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9bec55b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def even_fibo():\n",
    "    a, b = 1, 2\n",
    "    even = 0\n",
    "\n",
    "    while a <= 4000000:\n",
    "        if a % 2 == 0:\n",
    "            even += a\n",
    "        a, b = b, a + b\n",
    "\n",
    "    return even\n",
    "\n",
    "print(even_fibo())"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
