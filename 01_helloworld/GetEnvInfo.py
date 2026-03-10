import langchain
import langchain_community
import sys

if __name__ == "__main__":
    print("langchainVersion:  "+langchain.__version__)
    print("langchain_communityVersion:  "+langchain_community.__version__)
    print("langchainfile:"+langchain.__file__)

    print(sys.version)

