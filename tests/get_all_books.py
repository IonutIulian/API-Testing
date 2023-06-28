from requests_folder.get_books import get_all_books


class TestGetBooks:

    def test_get_books_nofilter_check_status_code(self):
        response = get_all_books()
        assert response.status_code==200, f"Error,status code is incorrect." \
                                          f"Expected 200, actual{response.status_code}"

    def test_get_books_nofilter_check_no_results(self):
        response = get_all_books()
        assert len(response.json())==6 ,f"Error, incorrect number" \
                                        f"of results, expected 6 ,actual {len(response.json())}"

    def test_get_books_filter_by_type_fiction(self):
        response = get_all_books("fiction")
        for i in range (len(response.json())):
            assert response.json()[i]["type"]=="fiction","Error, the filter did not work"


    def test_get_books_filter_by_type_non_fiction(self):
        response = get_all_books("non-fiction")
        for i in range (len(response.json())):
            assert response.json()[i]["type"]=="non-fiction","Error, the filter did not work"


    def test_get_books_filter_by_type_fiction_and_limit(self):
        response = get_all_books("fiction",3)
        for i in range (len(response.json())):
            assert response.json()[i]["type"]=="fiction","Error, the filter did not work"

        assert len(response.json())==3,f"Error, expected 3, actual{len(response.json())}"

    def test_get_books_filter_by_limit(self):
        response = get_all_books("",4)
        assert len(response.json()) == 4, f"Error, expected 4, actual{len(response.json())}"


