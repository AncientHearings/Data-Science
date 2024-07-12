{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPicd8/6Ln1hdWukCeS28Al",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AncientHearings/Data-Science/blob/main/numpyreshapingindexday4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VkAmoc551hHV"
      },
      "outputs": [],
      "source": [
        "#NumPy Reshaping\n",
        "#To change the shape of the array\n",
        "#Use reshape() method.\n",
        "#Two arguments are passed to it.\n",
        "#The First is row and the second is columns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np#Importing NumPy library\n"
      ],
      "metadata": {
        "id": "cJyk0iwm2P4R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "one=np.array([1,2,3,4,6,7,8,9,10,11,12,13,14,15,16])#One dimensional array\n",
        "print(one)\n",
        "np.ndim(one)#Dimensional method\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dl0C6KBB4DUG",
        "outputId": "baf48b85-b8ac-4bbb-a319-1180dd89e012"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 1  2  3  4  6  7  8  9 10 11 12 13 14 15 16]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Reshaping the array from one dimensinal to two two dimensional(rows and columns)\n",
        "#Use reshape method to which two arguments are passed :rows  number and column numbers\n",
        "two=one.reshape(3,5)\n",
        "print(two)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_ODV80iv4NrE",
        "outputId": "431df2b1-d80a-45cf-e01b-fb46c89cdb4d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ 1  2  3  4  6]\n",
            " [ 7  8  9 10 11]\n",
            " [12 13 14 15 16]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Reshaping array from one dimensional to three dimensional\n",
        "three=one.reshape(3,5,1)\n",
        "print(three)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cbTQoXC-4eBU",
        "outputId": "235d9c2b-f71f-4bbd-ca0c-70ca39ce44d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[ 1]\n",
            "  [ 2]\n",
            "  [ 3]\n",
            "  [ 4]\n",
            "  [ 6]]\n",
            "\n",
            " [[ 7]\n",
            "  [ 8]\n",
            "  [ 9]\n",
            "  [10]\n",
            "  [11]]\n",
            "\n",
            " [[12]\n",
            "  [13]\n",
            "  [14]\n",
            "  [15]\n",
            "  [16]]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Revision\n",
        "#Array reshaping is changing of shape.\n",
        "#To do that,use reshape method.\n",
        "#Associate with the array name.\n",
        "#Store it in a avariable.\n",
        "#To array() method,arguments are passed.\n",
        "#To convert into two dimensional,pass two arguments which are rows and columns.\n",
        "#To convert into three dimensional,pass three arguments which are rows,columns and number of elements in each row.\n",
        "#To know the dimenison of the array,use ndim() method."
      ],
      "metadata": {
        "id": "_fgo2FL96nZY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "QBT_EYAQBfaD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "one=np.array([1,2,3,4,5,6,7,8,9])#Creates a one dimensional array.\n",
        "print(one)#To call out the array\n",
        "np.ndim(one)#To ndim() method,argument is passed which is the array name(one)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tPqD6VeRBu0N",
        "outputId": "63ec9233-f68a-4059-8c42-78e38d2fc4c4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5 6 7 8 9]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "two=one.reshape(3,3)#To reshape into a two dimension\n",
        "print(two)\n",
        "np.ndim(two)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iQ0cz_AKB_ap",
        "outputId": "812252bb-d7dc-4561-8a99-bcef49a123a1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]\n",
            " [7 8 9]]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "three_dimensional=one.reshape(3,3,1)#To reshapoe into a three dimensional matrix\n",
        "print(three_dimensional)\n",
        "np.ndim(three_dimensional)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "90hdvBNWCeek",
        "outputId": "7f6d625d-fb77-48be-dbed-8e297d96b569"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[1]\n",
            "  [2]\n",
            "  [3]]\n",
            "\n",
            " [[4]\n",
            "  [5]\n",
            "  [6]]\n",
            "\n",
            " [[7]\n",
            "  [8]\n",
            "  [9]]]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "ARRAY INDEXING"
      ],
      "metadata": {
        "id": "xlSe0OrXC6o9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Items are indexed from 0.\n"
      ],
      "metadata": {
        "id": "u9E59gVbCscM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "one_dimensional_array=np.array([1,2,3,4,5,6])\n",
        "print(one_dimensional_array)\n",
        "print(f\"The number at second position is:{one_dimensional_array[2]}\")#Acessing 1D array"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wuT7p8ANDOHq",
        "outputId": "82e7d59b-144c-44ce-c10c-b59de9cd3959"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5 6]\n",
            "The number at second position is:3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "two_dimensional_array=np.array([[1,2,3],[4,5,6]])\n",
        "print(two_dimensional_array)\n",
        "print(f\"The element at 2nd row and 1st columns is: {two_dimensional_array[0,1]}\")#Acessing 2D array.Pass two arguments rows and columns.\n",
        "print(f\"The element at 2nd row and 2nd columns is: {two_dimensional_array[1,1]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WFTqpRH4DoQ2",
        "outputId": "a15641af-3849-477a-911e-4fe430fc7b28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]]\n",
            "The element at 2nd row and 1st columns is: 2\n",
            "The element at 2nd row and 2nd columns is: 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "three_dimensional_matrix=np.array([[[1,2,3],[4,5,6],[7,8,9]]])#Creates a three dimensional mtarix.\n",
        "print(three_dimensional_matrix)#To call out the three dimesional matrix.\n",
        "print(f\"The element in 0 matrix ,2nd row and 2nd column is : {three_dimensional_matrix[0,2,2]}\")#Aceesing element from three dimesnionalmatrix by specifying the matrix ,row and column\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "umyRjj8KD1XF",
        "outputId": "7dbe9503-c881-4331-a577-03fff6f11f51"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[1 2 3]\n",
            "  [4 5 6]\n",
            "  [7 8 9]]]\n",
            "The element in 0 matrix ,2nd row and 2nd column is : 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Revision\n",
        "#To call out the element of a 1D ,2D and 3D matrix ,we use array indexing.\n",
        "#Specify the position(s) within aquare brackets to access the element .\n",
        "#In case of 1D,specify the index.\n",
        "#In case of 2D ,specify the rwo and the column,\n",
        "#In case of 3D,specify the matrix,the row and the column.\n"
      ],
      "metadata": {
        "id": "jCi_6oT6G0g-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}