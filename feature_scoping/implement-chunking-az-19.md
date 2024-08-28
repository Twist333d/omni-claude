# Implement chunking

## Feature scope
- Process the input JSON data from FireCrawl
- Break down each page into meaningful chunks
- Generate summaries for each chunk using Claude 3 Haiku
- Output a structured JSON file with chunked and summarized content
- Prepare the output for embedding generation

## Input structure
The input is a JSON file containing scraped data from Supabase documentation. Each entry represents a page and includes:

base_url
timestamp
data (array of page objects)

content (raw HTML)
markdown (Markdown version of the content)
metadata (title, description, URL, etc.)

```json
{
  "base_url": "https://supabase.com/docs/",
  "timestamp": "2024-08-26T21:24:35.877974",
  "data": [
    {
      "content" : "Skipped for brevity",
       "markdown": "Javascript Reference v2.0\n\nPython Client Library\n=====================\n\nsupabase-py[View on GitHub](https://github.com/supabase/supabase-py)\n\nThis reference documents every object and method available in Supabase's Python library, [supabase-py](https://github.com/supabase/supabase-py)\n. You can use supabase-py to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.\n\n* * *\n\nInstalling\n----------\n\n### Install with PyPi[#](#install-with-pypi)\n\nYou can install supabase-py via the terminal. (for > Python 3.7)\n\nPIPConda\n\nTerminal\n\n`     _10  pip install supabase      `\n\n* * *\n\nInitializing\n------------\n\nYou can initialize a new Supabase client using the `create_client()` method.\n\nThe Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything we offer within the Supabase ecosystem.\n\n### Parameters\n\n*   supabase\\_urlRequiredstring\n    \n    The unique Supabase URL which is supplied when you create a new project in your project dashboard.\n    \n*   supabase\\_keyRequiredstring\n    \n    The unique Supabase Key which is supplied when you create a new project in your project dashboard.\n    \n*   optionsOptionalClientOptions\n    \n    Options to change the Auth behaviors.\n    \n    Details\n    \n\ncreate\\_client()With timeout option\n\n`     _10  import os  _10  from supabase import create_client, Client  _10  _10  url: str = os.environ.get(\"SUPABASE_URL\")  _10  key: str = os.environ.get(\"SUPABASE_KEY\")  _10  supabase: Client = create_client(url, key)      `\n\n* * *\n\nFetch data\n----------\n\n*   By default, Supabase projects return a maximum of 1,000 rows. This setting can be changed in your project's [API settings](/dashboard/project/_/settings/api)\n    . It's recommended that you keep it low to limit the payload size of accidental or malicious requests. You can use `range()` queries to paginate through your data.\n*   `select()` can be combined with [Filters](/docs/reference/python/using-filters)\n    \n*   `select()` can be combined with [Modifiers](/docs/reference/python/using-modifiers)\n    \n*   `apikey` is a reserved keyword if you're using the [Supabase Platform](/docs/guides/platform)\n     and [should be avoided as a column name](https://github.com/supabase/supabase/issues/5465)\n    .\n\n### Parameters\n\n*   columnsOptionalstring\n    \n    The columns to retrieve, defaults to `*`.\n    \n*   countOptionalCountMethod\n    \n    The property to use to get the count of rows returned.\n    \n\nGetting your dataSelecting specific columnsQuery referenced tablesQuery referenced tables through a join tableQuery the same referenced table multiple timesFiltering through referenced tablesQuerying referenced table with countQuerying with count optionQuerying JSON dataQuerying referenced table with inner joinSwitching schemas per query\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").execute()      `\n\nData source\n\nResponse\n\n* * *\n\nInsert data\n-----------\n\n### Parameters\n\n*   jsonRequireddict, list\n    \n    The values to insert. Pass an dict to insert a single row or an list to insert multiple rows.\n    \n*   countOptionalCountMethod\n    \n    The property to use to get the count of rows returned.\n    \n*   returningOptionalReturnMethod\n    \n    Either 'minimal' or 'representation'. Defaults to 'representation'.\n    \n*   default\\_to\\_nullOptionalbool\n    \n    Make missing fields default to `null`. Otherwise, use the default value for the column. Only applies for bulk inserts.\n    \n\nCreate a recordBulk create\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .insert({\"id\": 1, \"name\": \"Denmark\"})  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nUpdate data\n-----------\n\n*   `update()` should always be combined with [Filters](/docs/reference/python/using-filters)\n     to target the item(s) you wish to update.\n\n### Parameters\n\n*   jsonRequireddict, list\n    \n    The values to insert. Pass an dict to insert a single row or an list to insert multiple rows.\n    \n*   countOptionalCountMethod\n    \n    The property to use to get the count of rows returned.\n    \n\nUpdating your dataUpdating JSON data\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .update({\"name\": \"Australia\"})  _10  .eq(\"id\", 1)  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nUpsert data\n-----------\n\n*   Primary keys must be included in the `values` dict to use upsert.\n\n### Parameters\n\n*   jsonRequireddict, list\n    \n    The values to insert. Pass an dict to insert a single row or an list to insert multiple rows.\n    \n*   countOptionalCountMethod\n    \n    The property to use to get the count of rows returned.\n    \n*   returningOptionalReturnMethod\n    \n    Either 'minimal' or 'representation'. Defaults to 'representation'.\n    \n*   ignore\\_duplicatesOptionalbool\n    \n    Whether duplicate rows should be ignored.\n    \n*   on\\_conflictOptionalstring\n    \n    Specified columns to be made to work with UNIQUE constraint.\n    \n*   default\\_to\\_nullOptionalbool\n    \n    Make missing fields default to `null`. Otherwise, use the default value for the column. Only applies for bulk inserts.\n    \n\nUpsert your dataBulk Upsert your dataUpserting into tables with constraints\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .upsert({\"id\": 1, \"name\": \"Australia\"})  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nDelete data\n-----------\n\n*   `delete()` should always be combined with [filters](/docs/reference/python/using-filters)\n     to target the item(s) you wish to delete.\n*   If you use `delete()` with filters and you have [RLS](/docs/learn/auth-deep-dive/auth-row-level-security)\n     enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/`ALL` policy that makes the rows visible.\n*   When using `delete().in_()`, specify an array of values to target multiple rows with a single query. This is particularly useful for batch deleting entries that share common criteria, such as deleting users by their IDs. Ensure that the array you provide accurately represents all records you intend to delete to avoid unintended data removal.\n\n### Parameters\n\n*   countOptionalCountMethod\n    \n    The property to use to get the count of rows returned.\n    \n*   returningOptionalReturnMethod\n    \n    Either 'minimal' or 'representation'. Defaults to 'representation'.\n    \n\nDelete recordsDelete multiple records\n\n`     _10  response = supabase.table('countries').delete().eq('id', 1).execute()      `\n\nData source\n\nResponse\n\n* * *\n\nCall a Postgres function\n------------------------\n\nYou can call Postgres functions as _Remote Procedure Calls_, logic in your database that you can execute from anywhere. Functions are useful when the logic rarely changes\u2014like for password resets and updates.\n\n`     _10  create or replace function hello_world() returns text as $$  _10  select 'Hello world';  _10  $$ language sql;      `\n\n### Parameters\n\n*   fnRequiredcallable\n    \n    The stored procedure call to be executed.\n    \n*   paramsOptionaldict of any\n    \n    Parameters passed into the stored procedure call.\n    \n*   getOptionaldict of any\n    \n    When set to `true`, `data` will not be returned. Useful if you only need the count.\n    \n*   headOptionaldict of any\n    \n    When set to `true`, the function will be called with read-only access mode.\n    \n*   countOptionalCountMethod\n    \n    Count algorithm to use to count rows returned by the function. Only applicable for [set-returning functions](https://www.postgresql.org/docs/current/functions-srf.html)\n    . `\"exact\"`: Exact but slow count algorithm. Performs a `COUNT(*)` under the hood. `\"planned\"`: Approximated but fast count algorithm. Uses the Postgres statistics under the hood. `\"estimated\"`: Uses exact count for low numbers and planned count for high numbers.\n    \n\nCall a Postgres function without argumentsCall a Postgres function with argumentsBulk processingCall a Postgres function with filtersCall a read-only Postgres function\n\n`     _10  response = supabase.rpc(\"hello_world\").execute()      `\n\nData source\n\nResponse\n\n* * *\n\nUsing filters\n-------------\n\nFilters allow you to only return rows that match certain conditions.\n\nFilters can be used on `select()`, `update()`, `upsert()`, and `delete()` queries.\n\nIf a Postgres function returns a table response, you can also apply filters.\n\nApplying FiltersChainingConditional chainingFilter by values within JSON columnFilter Foreign Tables\n\n`     _15  # Correct  _15  response = (  _15  supabase.table(\"cities\")  _15  .select(\"name, country_id\")  _15  .eq(\"name\", \"Bali\")  _15  .execute()  _15  )  _15  _15  # Incorrect  _15  response = (  _15  supabase.table(\"cities\")  _15  .eq(\"name\", \"Bali\")  _15  .select(\"name, country_id\")  _15  .execute()  _15  )      `\n\nData source\n\nNotes\n\n* * *\n\nColumn is equal to a value\n--------------------------\n\nMatch only rows where `column` is equal to `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valueRequiredany\n    \n    The value to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").eq(\"name\", \"Albania\").execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn is not equal to a value\n------------------------------\n\nMatch only rows where `column` is not equal to `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valueRequiredany\n    \n    The value to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").neq(\"name\", \"Albania\").execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn is greater than a value\n------------------------------\n\nMatch only rows where `column` is greather than `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valueRequiredany\n    \n    The value to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").gt(\"id\", 2).execute()      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nColumn is greater than or equal to a value\n------------------------------------------\n\nMatch only rows where `column` is greater than or equal to `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valueRequiredany\n    \n    The value to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").gte(\"id\", 2).execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn is less than a value\n---------------------------\n\nMatch only rows where `column` is less than `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valueRequiredany\n    \n    The value to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").lt(\"id\", 2).execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn is less than or equal to a value\n---------------------------------------\n\nMatch only rows where `column` is less than or equal to `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valueRequiredany\n    \n    The value to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").lte(\"id\", 2).execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn matches a pattern\n------------------------\n\nMatch only rows where `column` matches `pattern` case-sensitively.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The name of the column to apply a filter on\n    \n*   patternRequiredstring\n    \n    The pattern to match by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").like(\"name\", \"%Alba%\").execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn matches a case-insensitive pattern\n-----------------------------------------\n\nMatch only rows where `column` matches `pattern` case-insensitively.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The name of the column to apply a filter on\n    \n*   patternRequiredstring\n    \n    The pattern to match by\n    \n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").ilike(\"name\", \"%alba%\").execute()      `\n\nData source\n\nResponse\n\n* * *\n\nColumn is a value\n-----------------\n\nMatch only rows where `column` IS `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The name of the column to apply a filter on\n    \n*   valueRequirednull | boolean\n    \n    The value to match by\n    \n\nChecking for nullness, True or False\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").is_(\"name\", \"null\").execute()      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nColumn is in an array\n---------------------\n\nMatch only rows where `column` is included in the `values` array.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valuesRequiredarray\n    \n    The values to filter by\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"*\")  _10  .in_(\"name\", [\"Albania\", \"Algeria\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nColumn contains every element in a value\n----------------------------------------\n\nOnly relevant for jsonb, array, and range columns. Match only rows where `column` contains every element appearing in `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   valuesRequiredobject\n    \n    The jsonb, array, or range value to filter with\n    \n\nOn array columnsOn range columnsOn \\`jsonb\\` columns\n\n`     _10  response = (  _10  supabase.table(\"issues\")  _10  .select(\"*\")  _10  .contains(\"tags\", [\"is:open\", \"priority:low\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nContained by value\n------------------\n\nOnly relevant for jsonb, array, and range columns. Match only rows where every element appearing in `column` is contained by `value`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The jsonb, array, or range column to filter on\n    \n*   valueRequiredobject\n    \n    The jsonb, array, or range value to filter with\n    \n\nOn array columnsOn range columnsOn \\`jsonb\\` columns\n\n`     _10  response = (  _10  supabase.table(\"classes\")  _10  .select(\"name\")  _10  .contained_by(\"days\", [\"monday\", \"tuesday\", \"wednesday\", \"friday\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nGreater than a range\n--------------------\n\nOnly relevant for range columns. Match only rows where every element in `column` is greater than any element in `range`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The range column to filter on\n    \n*   rangeRequiredarray\n    \n    The range to filter with\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"reservations\")  _10  .select(\"*\")  _10  .range_gt(\"during\", [\"2000-01-02 08:00\", \"2000-01-02 09:00\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nGreater than or equal to a range\n--------------------------------\n\nOnly relevant for range columns. Match only rows where every element in `column` is either contained in `range` or greater than any element in `range`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The range column to filter on\n    \n*   rangeRequiredstring\n    \n    The range to filter with\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"reservations\")  _10  .select(\"*\")  _10  .range_gte(\"during\", [\"2000-01-02 08:30\", \"2000-01-02 09:30\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nLess than a range\n-----------------\n\nOnly relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The range column to filter on\n    \n*   rangeRequiredarray\n    \n    The range to filter with\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"reservations\")  _10  .select(\"*\")  _10  .range_lt(\"during\", [\"2000-01-01 15:00\", \"2000-01-01 16:00\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nLess than or equal to a range\n-----------------------------\n\nOnly relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The range column to filter on\n    \n*   rangeRequiredarray\n    \n    The range to filter with\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"reservations\")  _10  .select(\"*\")  _10  .range_lte(\"during\", [\"2000-01-01 14:00\", \"2000-01-01 16:00\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nMutually exclusive to a range\n-----------------------------\n\nOnly relevant for range columns. Match only rows where `column` is mutually exclusive to `range` and there can be no element between the two ranges.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The range column to filter on\n    \n*   rangeRequiredarray\n    \n    The range to filter with\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"reservations\")  _10  .select(\"*\")  _10  .range_adjacent(\"during\", [\"2000-01-01 12:00\", \"2000-01-01 13:00\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nWith a common element\n---------------------\n\nOnly relevant for array and range columns. Match only rows where `column` and `value` have an element in common.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The array or range column to filter on\n    \n*   valueRequiredIterable\\[Any\\]\n    \n    The array or range value to filter with\n    \n\nOn array columnsOn range columns\n\n`     _10  response = (  _10  supabase.table(\"issues\")  _10  .select(\"title\")  _10  .overlaps(\"tags\", [\"is:closed\", \"severity:high\"])  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nMatch a string\n--------------\n\nOnly relevant for text and tsvector columns. Match only rows where `column` matches the query string in `query`.\n\n*   For more information, see [Postgres full text search](/docs/guides/database/full-text-search)\n    .\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The text or tsvector column to filter on\n    \n*   queryRequiredstring\n    \n    The query text to match with\n    \n*   optionsOptionalobject\n    \n    Named parameters\n    \n    Details\n    \n\nText searchBasic normalizationFull normalizationWebsearch\n\n`     _10  response = (  _10  supabase.table(\"texts\")  _10  .select(\"content\")  _10  .text_search(\"content\", \"'eggs' & 'ham'\", options={\"config\": \"english\"})  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nMatch an associated value\n-------------------------\n\nMatch only rows where each column in `query` keys is equal to its associated value. Shorthand for multiple `.eq()`s.\n\n### Parameters\n\n*   queryRequireddict\n    \n    The object to filter with, with column names as keys mapped to their filter values\n    \n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"*\")  _10  .match({\"id\": 2, \"name\": \"Albania\"})  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nDon't match the filter\n----------------------\n\nMatch only rows which doesn't satisfy the filter. `not_` expects you to use the raw PostgREST syntax for the filter values.\n\n``     _10  .not_.in_('id', '(5,6,7)') # Use `()` for `in` filter  _10  .not_.contains('arraycol', '\\{\"a\",\"b\"\\}') # Use `\\{\\}` for array values      ``\n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"*\")  _10  .not_.is_(\"name\", \"null\")  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nMatch at least one filter\n-------------------------\n\nor\\_() expects you to use the raw PostgREST syntax for the filter names and values.\n\n``     _10  .or_('id.in.(5,6,7), arraycol.cs.\\{\"a\",\"b\"\\}') # Use `()` for `in` filter, `\\{\\}` for array values and `cs` for `contains()`.  _10  .or_('id.in.(5,6,7), arraycol.cd.\\{\"a\",\"b\"\\}') # Use `cd` for `containedBy()`      ``\n\n### Parameters\n\n*   filtersRequiredstring\n    \n    The filters to use, following PostgREST syntax\n    \n*   reference\\_tableOptionalstring\n    \n    Set this to filter on referenced tables instead of the parent table\n    \n\nWith \\`select()\\`Use \\`or\\` with \\`and\\`Use \\`or\\` on referenced tables\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"name\")  _10  .or_(\"id.eq.2,name.eq.Algeria\")  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nMatch the filter\n----------------\n\nfilter() expects you to use the raw PostgREST syntax for the filter values.\n\n``     _10  .filter('id', 'in', '(5,6,7)') # Use `()` for `in` filter  _10  .filter('arraycol', 'cs', '\\{\"a\",\"b\"\\}') # Use `cs` for `contains()`, `\\{\\}` for array values      ``\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to filter on\n    \n*   operatorOptionalstring\n    \n    The operator to filter with, following PostgREST syntax\n    \n*   valueOptionalany\n    \n    The value to filter with, following PostgREST syntax\n    \n\nWith \\`select()\\`On a foreign table\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"*\")  _10  .filter(\"name\", \"in\", '(\"Algeria\",\"Japan\")')  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nUsing modifiers\n---------------\n\nFilters work on the row level\u2014they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition\u2014allowing you to change the format of the response (e.g., returning a CSV string).\n\nModifiers must be specified after filters. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).\n\n* * *\n\nOrder the results\n-----------------\n\nOrder the query result by `column`.\n\n### Parameters\n\n*   columnRequiredstring\n    \n    The column to order by\n    \n*   descOptionalbool\n    \n    Whether the rows should be ordered in descending order or not.\n    \n*   foreign\\_tableOptionalstring\n    \n    Foreign table name whose results are to be ordered.\n    \n*   nullsfirstOptionalbool\n    \n    Order by showing nulls first\n    \n\nWith \\`select()\\`On a foreign table\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"*\")  _10  .order(\"name\", desc=True)  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nLimit the number of rows returned\n---------------------------------\n\n### Parameters\n\n*   sizeRequirednumber\n    \n    The maximum number of rows to return\n    \n*   foreign\\_tableOptionalstring\n    \n    Set this to limit rows of foreign tables instead of the parent table.\n    \n\nWith \\`select()\\`On a foreign table\n\n`     _10  response = supabase.table(\"countries\").select(\"name\").limit(1).execute()      `\n\nData source\n\nResponse\n\n* * *\n\nLimit the query to a range\n--------------------------\n\nLimit the query result by starting at an offset (`from`) and ending at the offset (`from + to`). Only records within this range are returned. This respects the query order and if there is no order clause the range could behave unexpectedly.\n\nThe `from` and `to` values are 0-based and inclusive: `range(1, 3)` will include the second, third and fourth rows of the query.\n\n### Parameters\n\n*   startRequirednumber\n    \n    The starting index from which to limit the result.\n    \n*   endRequirednumber\n    \n    The last index to which to limit the result.\n    \n*   foreign\\_tableOptionalstring\n    \n    Set this to limit rows of foreign tables instead of the parent table.\n    \n\nWith \\`select()\\`On a foreign table\n\n`     _10  response = supabase.table(\"countries\").select(\"name\").range(0, 1).execute()      `\n\nData source\n\nResponse\n\n* * *\n\nRetrieve one row of data\n------------------------\n\nReturn `data` as a single object instead of an array of objects.\n\nWith \\`select()\\`\n\n`     _10  response = supabase.table(\"countries\").select(\"name\").limit(1).single().execute()      `\n\nData source\n\nResponse\n\n* * *\n\nRetrieve zero or one row of data\n--------------------------------\n\nReturn `data` as a single object instead of an array of objects.\n\nWith \\`select()\\`\n\n`     _10  response = (  _10  supabase.table(\"countries\")  _10  .select(\"*\")  _10  .eq(\"name\", \"Albania\")  _10  .maybe_single()  _10  .execute()  _10  )      `\n\nData source\n\nResponse\n\n* * *\n\nRetrieve as a CSV\n-----------------\n\nReturn `data` as a string in CSV format.\n\nReturn data as CSV\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").csv().execute()      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nUsing explain\n-------------\n\nFor debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html)\n of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.\n\nExplain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.\n\nFollow the [Performance Debugging Guide](/docs/guides/database/debugging-performance)\n to enable the functionality on your project.\n\n### Parameters\n\n*   walOptionalboolean\n    \n    If `true`, include information on WAL record generation.\n    \n*   verboseOptionalboolean\n    \n    If `true`, the query identifier will be returned and `data` will include the output columns of the query.\n    \n*   settingsOptionalboolean\n    \n    If `true`, include information on configuration parameters that affect query planning.\n    \n*   formatOptionalboolean\n    \n    The format of the output, can be `\"text\"` (default) or `\"json\"`.\n    \n*   formatOptional\"text\" | \"json\"\n    \n    The format of the output, can be `\"text\"` (default) or `\"json\"`.\n    \n*   buffersOptionalboolean\n    \n    If `true`, include information on buffer usage.\n    \n*   analyzeOptionalboolean\n    \n    If `true`, the query will be executed and the actual run time will be returned.\n    \n\nGet the execution planGet the execution plan with analyze and verbose\n\n`     _10  response = supabase.table(\"countries\").select(\"*\").explain().execute()      `\n\nData source\n\nResponse\n\nNotes\n\n* * *\n\nCreate a new user\n-----------------\n\n*   By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](https://supabase.com/dashboard/project/_/auth/providers)\n    .\n*   **Confirm email** determines if users need to confirm their email address after signing up.\n    *   If **Confirm email** is enabled, a `user` is returned but `session` is null.\n    *   If **Confirm email** is disabled, both a `user` and a `session` are returned.\n*   By default, when the user confirms their email address, they are redirected to the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls)\n    . You can modify your `SITE_URL` or add additional redirect URLs in [your project](https://supabase.com/dashboard/project/_/auth/url-configuration)\n    .\n*   If sign\\_up() is called for an existing confirmed user:\n    *   When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](/dashboard/project/_/auth/providers)\n        , an obfuscated/fake user object is returned.\n    *   When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.\n*   To fetch the currently logged-in user, refer to [`get_user()`](/docs/reference/python/auth-getuser)\n    .\n\n### Parameters\n\n*   credentialsRequiredSignUpWithPasswordCredentials\n    \n    Details\n    \n\nSign up with an email and passwordSign up with a phone number and password (SMS)Sign up with a phone number and password (whatsapp)Sign up with additional user metadataSign up with a redirect URL\n\n`     _10  response = supabase.auth.sign_up(  _10  {\"email\": \"email@example.com\", \"password\": \"password\"}  _10  )      `\n\nResponse\n\n* * *\n\nCreate an anonymous user\n------------------------\n\n*   Returns an anonymous user\n*   It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.\n\n### Parameters\n\n*   credentialsRequiredSignInAnonymouslyCredentials\n    \n    Details\n    \n\nCreate an anonymous userCreate an anonymous user with custom user metadata\n\n`     _10  response = supabase.auth.sign_in_anonymously(  _10  {\"options\": {\"captcha_token\": \"\"}}  _10  )      `\n\nResponse\n\n* * *\n\nSign in a user\n--------------\n\nLog in an existing user with an email and password or phone and password.\n\n*   Requires either an email and password or a phone number and password.\n\n### Parameters\n\n*   credentialsRequiredSignInWithPasswordCredentials\n    \n    Details\n    \n\nSign in with email and passwordSign in with phone and password\n\n`     _10  response = supabase.auth.sign_in_with_password(  _10  {\"email\": \"email@example.com\", \"password\": \"example-password\"}  _10  )      `\n\nResponse\n\n* * *\n\nSign in with ID Token\n---------------------\n\nAllows signing in with an OIDC ID token. The authentication provider used should be enabled and configured.\n\n### Parameters\n\n*   credentialsRequiredSignInWithIdTokenCredentials\n    \n    Details\n    \n\nSign In using ID Token\n\n`     _10  response = supabase.auth.sign_in_with_id_token(  _10  {\"provider\": \"google\", \"token\": \"your-id-token\"}  _10  )      `\n\nResponse\n\n* * *\n\nSign in a user through OTP\n--------------------------\n\n*   Requires either an email or phone number.\n*   This method is used for passwordless sign-ins where a OTP is sent to the user's email or phone number.\n*   If the user doesn't exist, `sign_in_with_otp()` will signup the user instead. To restrict this behavior, you can set `should_create_user` in `SignInWithPasswordlessCredentials.options` to `false`.\n*   If you're using an email, you can configure whether you want the user to receive a magiclink or a OTP.\n*   If you're using phone, you can configure whether you want the user to receive a OTP.\n*   The magic link's destination URL is determined by the [`SITE_URL`](/docs/guides/auth/redirect-urls)\n    .\n*   See [redirect URLs and wildcards](/docs/guides/auth/overview#redirect-urls-and-wildcards)\n     to add additional redirect URLs to your project.\n*   Magic links and OTPs share the same implementation. To send users a one-time code instead of a magic link, [modify the magic link email template](https://supabase.com/dashboard/project/_/auth/templates)\n     to include `\\{\\{ .Token \\}\\}` instead of `\\{\\{ .ConfirmationURL \\}\\}`.\n\n### Parameters\n\n*   credentialsRequiredSignInWithPasswordCredentials\n    \n    Details\n    \n\nSign in with emailSign in with SMS OTPSign in with WhatsApp OTP\n\n`     _10  response = supabase.auth.sign_in_with_otp(  _10  {  _10  \"email\": \"email@example.com\",  _10  \"options\": {\"email_redirect_to\": \"https://example.com/welcome\"},  _10  }  _10  )      `\n\nResponse\n\nNotes\n\n* * *\n\nSign in a user through OAuth\n----------------------------\n\n*   This method is used for signing in using a third-party provider.\n*   Supabase supports many different [third-party providers](/docs/guides/auth#configure-third-party-providers)\n    .\n\n### Parameters\n\n*   credentialsRequiredSignInWithOAuthCredentials\n    \n    Details\n    \n\nSign in using a third-party providerSign in using a third-party provider with redirectSign in with scopes\n\n`     _10  response = supabase.auth.sign_in_with_oauth({  _10  \"provider\": 'github'  _10  })      `\n\n* * *\n\nSign in a user through SSO\n--------------------------\n\n*   Before you can call this method you need to [establish a connection](/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections)\n     to an identity provider. Use the [CLI commands](/docs/reference/cli/supabase-sso)\n     to do this.\n*   If you've associated an email domain to the identity provider, you can use the `domain` property to start a sign-in flow.\n*   In case you need to use a different way to start the authentication flow with an identity provider, you can use the `provider_id` property. For example:\n    *   Mapping specific user email addresses with an identity provider.\n    *   Using different hints to identity the identity provider to be used by the user, like a company-specific page, IP address or other tracking information.\n\n### Parameters\n\n*   paramsRequiredSignInWithSSOCredentials\n    \n    Details\n    \n\nSign in with email domainSign in with provider UUID\n\n`     _10  response = supabase.auth.sign_in_with_sso({\"domain\": \"company.com\"})      `\n\nResponse\n\nNotes\n\n* * *\n\nSign out a user\n---------------\n\n*   In order to use the `sign_out()` method, the user needs to be signed in first.\n*   By default, `sign_out()` uses the global scope, which signs out all other sessions that the user is logged into as well.\n*   Since Supabase Auth uses JWTs for authentication, the access token JWT will be valid until it's expired. When the user signs out, Supabase revokes the refresh token and deletes the JWT from the client-side. This does not revoke the JWT and it will still be valid until it expires.\n\n### Parameters\n\n*   optionsOptionalSignOutOptions\n    \n    Details\n    \n\nSign out\n\n`     _10  response = supabase.auth.sign_out()      `\n\n* * *\n\nVerify and log in through OTP\n-----------------------------\n\n*   The `verify_otp` method takes in different verification types. If a phone number is used, the type can either be `sms` or `phone_change`. If an email address is used, the type can be one of the following: `email`, `recovery`, `invite` or `email_change` (`signup` and `magiclink` types are deprecated).\n*   The verification type used should be determined based on the corresponding auth method called before `verify_otp` to sign up / sign-in a user.\n*   The `TokenHash` is contained in the [email templates](/docs/guides/auth/auth-email-templates)\n     and can be used to sign in. You may wish to use the hash with Magic Links for the PKCE flow for Server Side Auth. See [this guide](/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)\n     for more details.\n\n### Parameters\n\n*   paramsRequiredVerifyOtpParams\n    \n    Details\n    \n\nVerify Signup One-Time Password (OTP)Verify SMS One-Time Password (OTP)Verify Email Auth (Token Hash)\n\n`     _10  response = supabase.auth.verify_otp(  _10  {\"email\": \"email@example.com\", \"token\": \"123456\", \"type\": \"email\"}  _10  )      `\n\nResponse\n\n* * *\n\nRetrieve a session\n------------------\n\n*   This method retrieves the current local session (i.e in memory).\n*   The session contains a signed JWT and unencoded session data.\n*   Since the unencoded session data is retrieved from the local storage medium, **do not** rely on it as a source of trusted data on the server. It could be tampered with by the sender. If you need verified, trustworthy user data, call [`get_user`](/docs/reference/python/auth-getuser)\n     instead.\n*   If the session has an expired access token, this method will use the refresh token to get a new session.\n\nGet the session data\n\n`     _10  response = supabase.auth.get_session()      `\n\nResponse\n\n* * *\n\nRetrieve a new session\n----------------------\n\nReturns a new session, regardless of expiry status. Takes in an optional refresh token. If not passed in, then refresh\\_session() will attempt to retrieve it from get\\_session(). If the current session's refresh token is invalid, an error will be thrown.\n\n*   This method will refresh the session whether the current one is expired or not.\n\n### Parameters\n\n*   refresh\\_tokenOptionalstring\n    \n\nRefresh session using the current session\n\n`     _10  response = supabase.auth.refresh_session()      `\n\nResponse\n\n* * *\n\nRetrieve a user\n---------------\n\n*   This method fetches the user object from the database instead of local session.\n*   This method is useful for checking if the user is authorized because it validates the user's access token JWT on the server.\n\n### Parameters\n\n*   jwtOptionalstring\n    \n    Takes in an optional access token JWT. If no JWT is provided, the JWT from the current session is used.\n    \n\nGet the logged in user with the current existing sessionGet the logged in user with a custom access token jwt\n\n`     _10  response = supabase.auth.get_user()      `\n\nResponse\n\n* * *\n\nSet the session data\n--------------------\n\nSets the session data from the current session. If the current session is expired, setSession will take care of refreshing it to obtain a new session. If the refresh token or access token in the current session is invalid, an error will be thrown.\n\n*   This method sets the session using an `access_token` and `refresh_token`.\n*   If successful, a `SIGNED_IN` event is emitted.\n\n### Parameters\n\n*   access\\_tokenRequiredstring\n    \n*   refresh\\_tokenRequiredstring\n    \n\nRefresh the session\n\n`     _10  response = supabase.auth.set_session(access_token, refresh_token)      `\n\nResponse\n\nNotes\n\n* * *\n\nAuth MFA\n--------\n\nThis section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.\n\nCurrently, we only support time-based one-time password (TOTP) as the 2nd factor. We don't support recovery codes but we allow users to enroll more than 1 TOTP factor, with an upper limit of 10.\n\nHaving a 2nd TOTP factor for recovery frees the user of the burden of having to store their recovery codes somewhere. It also reduces the attack surface since multiple recovery codes are usually generated compared to just having 1 backup TOTP factor.\n\n* * *\n\nEnroll a factor\n---------------\n\n*   Currently, `totp` is the only supported `factor_type`. The returned `id` should be used to create a challenge.\n*   To create a challenge, see [`mfa.challenge()`](/docs/reference/python/auth-mfa-challenge)\n    .\n*   To verify a challenge, see [`mfa.verify()`](/docs/reference/python/auth-mfa-verify)\n    .\n*   To create and verify a challenge in a single step, see [`mfa.challenge_and_verify()`](/docs/reference/python/auth-mfa-challengeandverify)\n    .\n\nEnroll a time-based, one-time password (TOTP) factor\n\n`     _10  res = supabase.auth.mfa.enroll({  _10  \"factor_type\": \"totp\",  _10  \"friendly_name\": \"your_friendly_name\"  _10  })      `\n\n* * *\n\nCreate a challenge\n------------------\n\n*   An [enrolled factor](/docs/reference/python/auth-mfa-enroll)\n     is required before creating a challenge.\n*   To verify a challenge, see [`mfa.verify()`](/docs/reference/python/auth-mfa-verify)\n    .\n\nCreate a challenge for a factor\n\n`     _10  res = supabase.auth.mfa.challenge({  _10  \"factor_id\": '34e770dd-9ff9-416c-87fa-43b31d7ef225'  _10  })      `\n\n* * *\n\nVerify a challenge\n------------------\n\n*   To verify a challenge, please [create a challenge](/docs/reference/python/auth-mfa-challenge)\n     first.\n\nVerify a challenge for a factor\n\n`     _10  res = supabase.auth.mfa.verify({  _10  \"factor_id\": '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  \"challenge_id\": '4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15',  _10  \"code\": '123456'  _10  })      `\n\n* * *\n\nCreate and verify a challenge\n-----------------------------\n\n*   An [enrolled factor](/docs/reference/python/auth-mfa-enroll)\n     is required before invoking `challengeAndVerify()`.\n*   Executes [`mfa.challenge()`](/docs/reference/python/auth-mfa-challenge)\n     and [`mfa.verify()`](/docs/reference/python/auth-mfa-verify)\n     in a single step.\n\nCreate and verify a challenge for a factor\n\n`     _10  res = supabase.auth.mfa.challenge_and_verify({  _10  \"factor_id\": '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  \"code\": '123456'  _10  })      `\n\n* * *\n\nUnenroll a factor\n-----------------\n\nUnenroll a factor\n\n`     _10  res = supabase.auth.mfa.unenroll({  _10  \"factor_id\": '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  })      `\n\n* * *\n\nGet Authenticator Assurance Level\n---------------------------------\n\n*   Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.\n*   In Supabase, having an AAL of `aal1` refers to having the 1st factor of authentication such as an email and password or OAuth sign-in while `aal2` refers to the 2nd factor of authentication such as a time-based, one-time-password (TOTP).\n*   If the user has a verified factor, the `next_level` field will return `aal2`, else, it will return `aal1`.\n\nGet the AAL details of a session\n\n`     _10  res = supabase.auth.mfa.get_authenticator_assurance_level()      `\n\n* * *\n\nInvokes a Supabase Edge Function.\n---------------------------------\n\nInvoke a Supabase Function.\n\n*   Requires an Authorization header.\n*   When you pass in a body to your function, we automatically attach the Content-Type header for `Blob`, `ArrayBuffer`, `File`, `FormData` and `String`. If it doesn't match any of these types we assume the payload is `json`, serialise it and attach the `Content-Type` header as `application/json`. You can override this behaviour by passing in a `Content-Type` header of your own.\n\nBasic invocationError handlingPassing custom headers\n\n`     _10  response = supabase.functions.invoke(  _10  \"hello-world\", invoke_options={\"body\": {\"name\": \"Functions\"}}  _10  )      `\n\n* * *\n\nSubscribe to channel\n--------------------\n\n*   By default, Broadcast and Presence are enabled for all projects.\n*   By default, listening to database changes is disabled for new projects due to database performance and security concerns. You can turn it on by managing Realtime's [replication](/docs/guides/api#realtime-api-overview)\n    .\n*   You can receive the \"previous\" data for updates and deletes by setting the table's `REPLICA IDENTITY` to `FULL` (e.g., `ALTER TABLE your_table REPLICA IDENTITY FULL;`).\n*   Row level security is not applied to delete statements. When RLS is enabled and replica identity is set to full, only the primary key is sent to clients.\n\nListen to broadcast messagesListen to presence syncListen to presence joinListen to presence leaveListen to all database changesListen to a specific tableListen to insertsListen to updatesListen to deletesListen to multiple eventsListen to row level changes\n\n`     _10  channel = supabase.channel(\"room1\")  _10  _10  def on_subscribe(status, err):  _10  if status == RealtimeSubscribeStates.SUBSCRIBED:  _10  channel.send_broadcast('cursor-pos', { \"x\": random.random(), \"y\": random.random() })  _10  _10  def handle_broadcast(payload):  _10  print(\"Cursor position received!\", payload)  _10  _10  channel.on_broadcast(event=\"cursor-pos\", callback=handle_broadcast).subscribe(on_subscribe)      `\n\n* * *\n\nUnsubscribe from a channel\n--------------------------\n\n*   Removing a channel is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.\n\nRemoves a channel\n\n`     _10  supabase.remove_channel(myChannel)      `\n\n* * *\n\nUnsubscribe from all channels\n-----------------------------\n\n*   Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.\n\nRemove all channels\n\n`     _10  supabase.remove_all_channels()      `\n\n* * *\n\nRetrieve all channels\n---------------------\n\nGet all channels\n\n`     _10  channels = supabase.get_channels()      `\n\n* * *\n\nBroadcast a message\n-------------------\n\nBroadcast a message to all connected clients to a channel.\n\nSend a message via websocket\n\n`     _10  channel = supabase.channel('room1')  _10  _10  def on_subscribe(status, err):  _10  if status == RealtimeSubscribeStates.SUBSCRIBED:  _10  channel.send_broadcast('cursor-pos', { \"x\": random.random(), \"y\": random.random() })  _10  _10  channel.subscribe(on_subscribe)      `\n\nResponse\n\n* * *\n\nCreate a bucket\n---------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: `insert`\n    *   `objects` table permissions: none\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nCreate bucket\n\n`     _10  res = supabase.storage.create_bucket(name)      `\n\n* * *\n\nRetrieve a bucket\n-----------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: `select`\n    *   `objects` table permissions: none\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nGet bucket\n\n`     _10  res = supabase.storage.get_bucket(name)      `\n\n* * *\n\nList all buckets\n----------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: `select`\n    *   `objects` table permissions: none\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nList buckets\n\n`     _10  res = supabase.storage.list_buckets()      `\n\n* * *\n\nDelete a bucket\n---------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: `select` and `delete`\n    *   `objects` table permissions: none\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nDelete bucket\n\n`     _10  res = supabase.storage.delete_bucket(name)      `\n\n* * *\n\nEmpty a bucket\n--------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: `select`\n    *   `objects` table permissions: `select` and `delete`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nEmpty bucket\n\n`     _10  res = supabase.storage.empty_bucket(name)      `\n\n* * *\n\nUpload a file\n-------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `insert`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n*   Please specify the appropriate content [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)\n     if you are uploading images or audio. If no `file_options` are specified, the MIME type defaults to `text/html`.\n\nUpload file using filepath\n\n`     _10  with open(filepath, 'rb') as f:  _10  supabase.storage.from_(\"testbucket\").upload(file=f,path=path_on_supastorage, file_options={\"content-type\": \"audio/mpeg\"})      `\n\n* * *\n\nDownload a file\n---------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `select`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nDownload file\n\n`     _10  with open(destination, 'wb+') as f:  _10  res = supabase.storage.from_('bucket_name').download(source)  _10  f.write(res)      `\n\n* * *\n\nList all files in a bucket\n--------------------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `select`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nList files in a bucket\n\n`     _10  res = supabase.storage.from_('bucket_name').list()      `\n\n* * *\n\nReplace an existing file\n------------------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `update` and `select`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nUpdate file\n\n`     _10  with open(filepath, 'rb') as f:  _10  supabase.storage.from_(\"bucket_name\").update(file=f, path=path_on_supastorage, file_options={\"cache-control\": \"3600\", \"upsert\": \"true\"})      `\n\n* * *\n\nMove an existing file\n---------------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `update` and `select`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nMove file\n\n`     _10  res = supabase.storage.from_('bucket_name').move('public/avatar1.png', 'private/avatar2.png')      `\n\n* * *\n\nDelete files in a bucket\n------------------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `delete` and `select`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nDelete file\n\n`     _10  res = supabase.storage.from_('bucket_name').remove('test.jpg')      `\n\n* * *\n\nCreate a signed URL\n-------------------\n\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: `select`\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nCreate Signed URL\n\n`     _10  res = supabase.storage.from_('bucket_name').create_signed_url(filepath, expiry_duration)      `\n\n* * *\n\nRetrieve public URL\n-------------------\n\n*   The bucket needs to be set to public, either via [updateBucket()](/docs/reference/python/storage-updatebucket)\n     or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard)\n    , clicking the overflow menu on a bucket and choosing \"Make public\"\n*   RLS policy permissions required:\n    *   `buckets` table permissions: none\n    *   `objects` table permissions: none\n*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\n     on how access control works\n\nReturns the URL for an asset in a public bucket\n\n`     _10  res = supabase.storage.from_('bucket_name').get_public_url('test/avatar1.jpg')      `",
      "metadata": {
        "ogUrl": "https://supabase.com/docs/reference/python/python",
        "title": "Python API Reference | Supabase Docs",
        "robots": "index, follow",
        "ogImage": "https://obuldanrptloktxcffvn.supabase.co/functions/v1/og-images?site=docs&type=API%20Reference&title=Python&description=undefined",
        "ogTitle": "Python API Reference | Supabase Docs",
        "sourceURL": "https://supabase.com/docs/reference/python/initializing",
        "description": "API reference for the Python Supabase SDK",
        "modifiedTime": "2024-08-26T15:58:16.181Z",
        "ogDescription": "API reference for the Python Supabase SDK",
        "publishedTime": "2024-08-26T15:58:16.181Z",
        "pageStatusCode": 200,
        "ogLocaleAlternate": []
      },
      "linksOnPage": [],
```

## Example RAG from Anthropic RAG tutorial
URL: https://github.com/anthropics/anthropic-cookbook/blob/main/skills/retrieval_augmented_generation/guide.ipynb

### Chunk structure
This is the structure of the docs they used in Anthropic tutorial on RAG.
```json
[
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#get-started",
    "chunk_heading": "Get started",
    "text": "Get started\n\n\nIf you\u2019re new to Claude, start here to learn the essentials and make your first API call.\nIntro to ClaudeExplore Claude\u2019s capabilities and development flow.QuickstartLearn how to make your first API call in minutes.Prompt LibraryExplore example prompts for inspiration.\nIntro to ClaudeExplore Claude\u2019s capabilities and development flow.\n\nIntro to Claude\nExplore Claude\u2019s capabilities and development flow.\nQuickstartLearn how to make your first API call in minutes.\n\nQuickstart\nLearn how to make your first API call in minutes.\nPrompt LibraryExplore example prompts for inspiration.\n\nPrompt Library\nExplore example prompts for inspiration.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#models",
    "chunk_heading": "Models",
    "text": "Models\n\n\nClaude consists of a family of large language models that enable you to balance intelligence, speed, and cost.\n\n\n\n\n\nCompare our state-of-the-art models.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#develop-with-claude",
    "chunk_heading": "Develop with Claude",
    "text": "Develop with Claude\n\n\nAnthropic has best-in-class developer tools to build scalable applications with Claude.\nDeveloper ConsoleEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.API ReferenceExplore, implement, and scale with the Anthropic API and SDKs.Anthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.\nDeveloper ConsoleEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.\n\nDeveloper Console\nEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.\nAPI ReferenceExplore, implement, and scale with the Anthropic API and SDKs.\n\nAPI Reference\nExplore, implement, and scale with the Anthropic API and SDKs.\nAnthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.\n\nAnthropic Cookbook\nLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#key-capabilities",
    "chunk_heading": "Key capabilities",
    "text": "Key capabilities\n\n\nClaude can assist with many tasks that involve text, code, and images.\nText and code generationSummarize text, answer questions, extract data, translate text, and explain and generate code.VisionProcess and analyze visual input and generate text and code from images.\nText and code generationSummarize text, answer questions, extract data, translate text, and explain and generate code.\n\nText and code generation\nSummarize text, answer questions, extract data, translate text, and explain and generate code.\nVisionProcess and analyze visual input and generate text and code from images.\n\nVision\nProcess and analyze visual input and generate text and code from images.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#support",
    "chunk_heading": "Support",
    "text": "Support\n\n\nHelp CenterFind answers to frequently asked account and billing questions.Service StatusCheck the status of Anthropic services.\nHelp CenterFind answers to frequently asked account and billing questions.\n\nHelp Center\nFind answers to frequently asked account and billing questions.\nService StatusCheck the status of Anthropic services.\n\nService Status\nCheck the status of Anthropic services.\nQuickstartxlinkedin\nQuickstart\nxlinkedin\nGet started Models Develop with Claude Key capabilities Support\nGet startedModelsDevelop with ClaudeKey capabilitiesSupport\n"
  },
```

So each chunk has:
- chunk_link -> seems like they broke it by sections.
- chunk_heading -> which seems to be the section name.
- text: text of the chunk

### Embedding approach
```python
def load_data(self, data):
        if self.embeddings and self.metadata:
            print("Vector database is already loaded. Skipping data loading.")
            return
        if os.path.exists(self.db_path):
            print("Loading vector database from disk.")
            self.load_db()
            return

        texts = [f"Heading: {item['chunk_heading']}\n\n Chunk Text:{item['text']}" for item in data]
        self._embed_and_store(texts, data)
        self.save_db()
        print("Vector database loaded and saved.")
```

So how did they create each chunk for embeddings:
- they created a list where each chunk had it's heading + text
- then they passed it into the embedding model
- later they added summary of the heading + text and appending 'summary' to the chunk

Final chunk structure is:
```python
summarized_doc = {
    "chunk_link": doc["chunk_link"],
    "chunk_heading": doc["chunk_heading"],
    "text": doc["text"],
    "summary": summary
}
```

Summary was generated by the model using this approach:
```python
def generate_summaries(input_file, output_file):
 
    # Load the original documents
    with open(input_file, 'r') as f:
        docs = json.load(f)

    # Prepare the context about the overall knowledge base
    knowledge_base_context = "This is documentation for Anthropic's, a frontier AI lab building Claude, an LLM that excels at a variety of general purpose tasks. These docs contain model details and documentation on Anthropic's APIs."

    summarized_docs = []

    for doc in tqdm(docs, desc="Generating summaries"):
        prompt = f"""
        You are tasked with creating a short summary of the following content from Anthropic's documentation. 

        Context about the knowledge base:
        {knowledge_base_context}

        Content to summarize:
        Heading: {doc['chunk_heading']}
        {doc['text']}

        Please provide a brief summary of the above content in 2-3 sentences. The summary should capture the key points and be concise. We will be using it as a key part of our search pipeline when answering user queries about this content. 

        Avoid using any preamble whatsoever in your response. Statements such as 'here is the summary' or 'the summary is as follows' are prohibited. You should get straight into the summary itself and be concise. Every word matters.
        """

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=150,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        summary = response.content[0].text.strip()

        summarized_doc = {
            "chunk_link": doc["chunk_link"],
            "chunk_heading": doc["chunk_heading"],
            "text": doc["text"],
            "summary": summary
        }
        summarized_docs.append(summarized_doc)

    # Save the summarized documents to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(summarized_docs, f, indent=2)

    print(f"Summaries generated and saved to {output_file}")

# generate_summaries('data/anthropic_docs.json', 'data/anthropic_summary_indexed_docs.json')
```
Summary increased the key metrics of RAG by either small or medium amount (specifically recall increased from 0.56 
to 0.71)

## Output that we need for embeddings

The output will be a json file containing an array of chunk objects (dictionaries). Each chunk object will have the 
following structure:

```json
{
  "chunk_id": "unique_identifier",
  "source_url": "https://supabase.com/docs/path/to/page",
  "main_heading": "H1 or H2 heading text",
  "content": "Full content including lower-level headings and all markdown formatting",
  "summary": "Brief summary generated by Claude 3 Haiku"
}
```

## Document Structure
- Main headings (h1 underlined with equals signs, h2 underlined with dashes)
- Subheadings (h3 and below, prefixed with ###)
- Content (including parameters, code blocks, and examples)
- Separators (* * *)

## Chunking Strategy

1. **Main Chunks**
   - Each h1 or h2 heading starts a new chunk
   - Content following the heading, up to the next h1 or h2 heading or separator (* * *), is included in the chunk
   - Use the markdown library to accurately identify heading levels

2. **Content Handling**
   - All content (including subheadings, code blocks, lists, and examples) is treated as text within its respective main chunk
   - Formatting is preserved to maintain the original structure
   - Subheadings (h3 and below) are preserved within the content of their parent chunk

3. **Special Cases**
   - Code blocks: Preserve backtick formatting
   - Lists: Maintain indentation and bullet points/numbering
   - Tables: Preserve table structure
   - Links: Maintain link structure and URL
   - Emphasis: Preserve bold and italic formatting

4. **Chunk Size Control**
   - Implement soft token limits (800-1200 tokens) for each chunk
   - If a chunk exceeds the upper limit:
     - Attempt to split at the next h3 or lower heading within the chunk
     - If no suitable heading is found, split at the next paragraph break
   - Allow for a +/- 20% tolerance on the token limit to avoid unnecessary splits

## Processing Steps

1. **Load Data**
   - Read the JSON file containing scraped markdown content

2. **Parse Markdown**
   - Use the markdown library to parse the document and identify all headings and their levels

3. **Identify and Process Chunks**
   - Iterate through the parsed structure:
     - Create new chunks for h1 and h2 headings
     - Include all content and lower-level headings within each chunk
     - Extract main heading
     - Capture all content, preserving formatting
     - Generate a unique ID
     - Record source URL
   - Check token count and split if necessary, following the chunk size control rules

4. **Generate Summaries**
   - Use Claude 3 Haiku to create concise summaries for each chunk

5. **Format Output**
   - Create JSON objects for each chunk
   - Combine into a final JSON array

6. **Validate Output**
   - Ensure all content is captured
   - Verify chunk structure and completeness
   - Check that total content matches the original input

## Modular Structure

1. DataLoader
   - load_json_data()

2. MarkdownParser
   - parse_markdown()

3. ChunkIdentifier
   - identify_chunks()

4. ChunkProcessor
   - process_chunk()
   - split_large_chunks()
   - extract_subheadings()

5. TokenCounter
   - count_tokens()

6. SummaryGenerator
   - generate_summary()

7. OutputFormatter
   - create_chunk_object()
   - generate_json_output()

8. Validator
   - validate_completeness()
   - validate_structure()

9. MainProcessor
   - orchestrate_chunking()
   - handle_errors()

## Implementation Considerations
- Use the markdown library for parsing and maintaining document structure
- Implement token counting using tiktoken for accurate token counts
- Ensure code blocks and other special elements are not split across chunks
- Implement error handling and logging for edge cases
- Use regex only as a fallback for identifying main headings if the markdown parsing fails



# Iterations 
## Iteration #2 comments
**Good points**
- H1 headings distinction: You're correct. Looking at the example chunks, we are indeed 
  correctly identifying and splitting at H1 headers, regardless of whether they're marked with '===' or '#'. The current implementation is working as intended, and we don't need to make any changes here. Thank you for pointing this out.
- Separators: Understood. We'll ignore the separators (* * *) and not handle them in any special 
  way.


Features yet to implement:
- Token counting and chunk size control
- Splitting large chunks if they exceed a token limit
- Summary generation for each chunk
- Validation of the output (completeness and structure)
- Processing of multiple pages (if required in the future)


## Additional changes
## Agreed Changes and Additions

### 1. Implement More Lenient vs More Strict Validation Rules

- Strict rules (raise errors):
  - Each chunk must have the required structure (all necessary fields)
  - The total number of h1 and h2 headings in chunks should match the original document

- Lenient rules (log warnings):
  - Content length differences between original and processed content (with a threshold, e.g., 5% difference)

### 2. Implement Chunk Splitting

- Prioritize splitting at logical boundaries:
  1. Try to split at subheadings (h3, h4, etc.)
  2. If no subheadings, split at paragraph boundaries
  3. As a last resort, split at sentence boundaries
- Implement a "soft" token limit (allow exceeding by 20%)
- Look for "signals" of important content (e.g., code blocks, list structures)
- Include a small overlap (1-2 sentences) between split chunks

### 3. Enhance Summary Statistics

- Report the total number of chunks created
- Show approximate token counts for chunks (min, max, average)
- Display character counts for chunks (min, max, average)
- Report the number of h1, h2, and h3 headings found
- Show the distribution of chunk sizes (e.g., how many are within different ranges)