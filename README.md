## Amazon Bedrock - Introductory Demo

Amazon Bedrock is a **fully managed** service that offers **API access** to a choice of high-performing **foundation models** (FMs) from leading AI companies
including AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon, along with a broad set of capabilities that you need to build generative AI applications, **simplifying** development while maintaining **privacy** and **security**. 

This demo provides a basic introduction to some GenAI use cases, by allowing you to interact with FMs using Amazon Bedrock. This demo application is intended for **quick deployment** on your workstation to allow you explore Amazon Bedrock easily.

Watch a video of the demo below (the **Chrome** browser is recommended)! 

https://github.com/aws-samples/amazon-bedrock-intro-demo/assets/39437216/d8412353-0ad3-4809-8b6b-b5d5116d559f

**NOTE:** Refer to the [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) to understand the costs incurred with using Amazon Bedrock.

### Prerequisites
- AWS account (sandbox account recommended)
- IAM user or role with Administrator access or the [required permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html) to access Amazon Bedrock and its FMs. Configure this principal's credentials in your environment's [default AWS profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) (AWS_PROFILE).
- Python 3.9+
- Linux (preferred)
- Internet access

### Getting started
Implement the following steps to start using the demo application:

**STEP 1:** Create a Python virtual environment 

```
python -m venv demo
cd demo
source bin/activate
```

**STEP 2:** Clone the git repository

```
git clone https://github.com/aws-samples/amazon-bedrock-intro-demo.git
```

Alternatively, download the code and extract the amazon-bedrock-intro-demo directory.

**STEP 3:** Install the required python modules 

```
cd amazon-bedrock-intro-demo
pip install -r requirements.txt
```

**STEP 4:** Launch the Streamlit application and access the displayed URL

```
streamlit run main.py
```
