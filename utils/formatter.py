def print_sources(results):

    print("\nSources\n")

    for result in results:

        print("=" * 70)

        print(f"Document : {result.payload['document']}")

        print(f"Page     : {result.payload['page']}")

        print("\nRetrieved Text:\n")

        print(result.payload["text"])

        print("=" * 70)