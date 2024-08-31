# https://supabase.com/docs/faq
[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

*   [Start](/docs/guides/getting-started)
    
*   Products
*   Build
*   Reference
*   Resources

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

Search docs...

K

### Where do I find support?

Choose the support channel relevant for your situation here: [supabase.com/support](https://supabase.com/support)

### How much does it cost?

Self-hosting Supabase is free. If you wish to use our cloud-platform, we provide [simple, predictable pricing](https://supabase.com/pricing)
.

### How do I host Supabase?

You can use the docker compose script [here](https://github.com/supabase/supabase/tree/master/docker)
, and find detailed instructions [here](/docs/guides/hosting/overview)
.

Supabase is an amalgamation of open source tools. Some of these tools are made by Supabase (like our [Realtime Server](https://github.com/supabase/realtime)
), some we support directly (like [PostgREST](http://postgrest.org/en/v7.0.0/)
), and some are third-party tools (like [KonSupabase is an amalgamation open sourceg](https://github.com/Kong/kong)
).

All of the tools we use in Supabase are MIT, Apache 2.0, or PostgreSQL licensed. This is one of the requirements to be considered for the Supabase stack.

### How can you be a Firebase alternative if you're built with a relational database?

We started Supabase because we love the functionality of Firebase, but we personally experienced the scaling issues that many others experienced. We chose Postgres because it's well-trusted, with phenomenal scalability.

Our goal is to make Postgres as easy to use as Firebase, so that you no longer have to choose between usability and scalability. We're sure that once you start using Postgres, you'll love it more than any other database.

### Do you support `[some other database]`?

We only support PostgreSQL. It's unlikely we'll ever move away from Postgres; however, you can [vote on a new database](https://github.com/supabase/supabase/discussions/6)
 if you want us to start development.

### Do you have a library for `[some other language]`?

We officially support [JavaScript](/docs/reference/javascript/installing)
, [Swift](/docs/reference/swift/installing)
, and [Flutter](/docs/reference/dart/installing)
.

You can find community-supported libraries including Python, C#, PHP, and Ruby in our [GitHub Community](https://github.com/supabase-community)
, and you can also help us to identify the most popular languages by [voting for a new client library](https://github.com/supabase/supabase/discussions/5)
.

*   Need some help?
    
    [Contact support](https://supabase.com/support)
    
*   Latest product updates?
    
    [See Changelog](https://supabase.com/changelog)
    
*   Something's not right?
    
    [Check system status](https://status.supabase.com/)
    

* * *

[© Supabase Inc](https://supabase.com/)
—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)
[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)
[Open Source](https://supabase.com/open-source)
[SupaSquad](https://supabase.com/supasquad)
Privacy Settings

[GitHub](https://github.com/supabase/supabase)
[Twitter](https://twitter.com/supabase)
[Discord](https://discord.supabase.com/)

# https://supabase.com/docs/reference/javascript/initializing
[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

*   [Start](/docs/guides/getting-started)
    
*   Products
*   Build
*   Reference
*   Resources

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

Search docs...

K

Main menu

JavaScript

v2.0

*   [Introduction](/docs/reference/javascript/introduction)
    
*   [Installing](/docs/reference/javascript/installing)
    
*   [Initializing](/docs/reference/javascript/initializing)
    
*   [TypeScript support](/docs/reference/javascript/typescript-support)
    
*   * * *
    
    Database
    
    *   [Fetch data](/docs/reference/javascript/select)
        
    *   [Insert data](/docs/reference/javascript/insert)
        
    *   [Update data](/docs/reference/javascript/update)
        
    *   [Upsert data](/docs/reference/javascript/upsert)
        
    *   [Delete data](/docs/reference/javascript/delete)
        
    *   [Call a Postgres function](/docs/reference/javascript/rpc)
        
    *   Using filters
        
    *   Using modifiers
        
*   * * *
    
    Auth
    
    *   [Overview](/docs/reference/javascript/auth-api)
        
    *   [Error codes](/docs/reference/javascript/auth-error-codes)
        
    *   [Create a new user](/docs/reference/javascript/auth-signup)
        
    *   [Listen to auth events](/docs/reference/javascript/auth-onauthstatechange)
        
    *   [Create an anonymous user](/docs/reference/javascript/auth-signinanonymously)
        
    *   [Sign in a user](/docs/reference/javascript/auth-signinwithpassword)
        
    *   [Sign in with ID Token](/docs/reference/javascript/auth-signinwithidtoken)
        
    *   [Sign in a user through OTP](/docs/reference/javascript/auth-signinwithotp)
        
    *   [Sign in a user through OAuth](/docs/reference/javascript/auth-signinwithoauth)
        
    *   [Sign in a user through SSO](/docs/reference/javascript/auth-signinwithsso)
        
    *   [Sign out a user](/docs/reference/javascript/auth-signout)
        
    *   [Send a password reset request](/docs/reference/javascript/auth-resetpasswordforemail)
        
    *   [Verify and log in through OTP](/docs/reference/javascript/auth-verifyotp)
        
    *   [Retrieve a session](/docs/reference/javascript/auth-getsession)
        
    *   [Retrieve a new session](/docs/reference/javascript/auth-refreshsession)
        
    *   [Retrieve a user](/docs/reference/javascript/auth-getuser)
        
    *   [Update a user](/docs/reference/javascript/auth-updateuser)
        
    *   [Retrieve identities linked to a user](/docs/reference/javascript/auth-getuseridentities)
        
    *   [Link an identity to a user](/docs/reference/javascript/auth-linkidentity)
        
    *   [Unlink an identity from a user](/docs/reference/javascript/auth-unlinkidentity)
        
    *   [Send a password reauthentication nonce](/docs/reference/javascript/auth-reauthentication)
        
    *   [Resend an OTP](/docs/reference/javascript/auth-resend)
        
    *   [Set the session data](/docs/reference/javascript/auth-setsession)
        
    *   [Exchange an auth code for a session](/docs/reference/javascript/auth-exchangecodeforsession)
        
    *   [Start auto-refresh session (non-browser)](/docs/reference/javascript/auth-startautorefresh)
        
    *   [Stop auto-refresh session (non-browser)](/docs/reference/javascript/auth-stopautorefresh)
        
    *   Auth MFA
        
    *   Auth Admin
        
*   * * *
    
    Edge Functions
    
    *   [Invokes a Supabase Edge Function.](/docs/reference/javascript/functions-invoke)
        
*   * * *
    
    Realtime
    
    *   [Subscribe to channel](/docs/reference/javascript/subscribe)
        
    *   [Unsubscribe from a channel](/docs/reference/javascript/removechannel)
        
    *   [Unsubscribe from all channels](/docs/reference/javascript/removeallchannels)
        
    *   [Retrieve all channels](/docs/reference/javascript/getchannels)
        
    *   [Broadcast a message](/docs/reference/javascript/broadcastmessage)
        
*   * * *
    
    Storage
    
    *   [Create a bucket](/docs/reference/javascript/storage-createbucket)
        
    *   [Retrieve a bucket](/docs/reference/javascript/storage-getbucket)
        
    *   [List all buckets](/docs/reference/javascript/storage-listbuckets)
        
    *   [Update a bucket](/docs/reference/javascript/storage-updatebucket)
        
    *   [Delete a bucket](/docs/reference/javascript/storage-deletebucket)
        
    *   [Empty a bucket](/docs/reference/javascript/storage-emptybucket)
        
    *   [Upload a file](/docs/reference/javascript/storage-from-upload)
        
    *   [Download a file](/docs/reference/javascript/storage-from-download)
        
    *   [List all files in a bucket](/docs/reference/javascript/storage-from-list)
        
    *   [Replace an existing file](/docs/reference/javascript/storage-from-update)
        
    *   [Move an existing file](/docs/reference/javascript/storage-from-move)
        
    *   [Copy an existing file](/docs/reference/javascript/storage-from-copy)
        
    *   [Delete files in a bucket](/docs/reference/javascript/storage-from-remove)
        
    *   [Create a signed URL](/docs/reference/javascript/storage-from-createsignedurl)
        
    *   [Create signed URLs](/docs/reference/javascript/storage-from-createsignedurls)
        
    *   [Create signed upload URL](/docs/reference/javascript/storage-from-createsigneduploadurl)
        
    *   [Upload to a signed URL](/docs/reference/javascript/storage-from-uploadtosignedurl)
        
    *   [Retrieve public URL](/docs/reference/javascript/storage-from-getpublicurl)
        
*   * * *
    
    Misc
    
    *   [Release Notes](/docs/reference/javascript/release-notes)
        

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

*   [Start](/docs/guides/getting-started)
    
*   Products
*   Build
*   Reference
*   Resources

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

Search docs...

K

Javascript Reference v2.0

JavaScript Client Library
=========================

@supabase/supabase-js[View on GitHub](https://github.com/supabase/supabase-js)

This reference documents every object and method available in Supabase's isomorphic JavaScript library, `supabase-js`. You can use `supabase-js` to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.

* * *

Installing
----------

### Install as package[#](#install-as-package)

You can install @supabase/supabase-js via the terminal.

npmYarnpnpm

Terminal

`     _10  npm install @supabase/supabase-js      `

### Install via CDN[#](#install-via-cdn)

You can install @supabase/supabase-js via CDN links.

`     _10  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>  _10  //or  _10  <script src="https://unpkg.com/@supabase/supabase-js@2"></script>      `

### Use at runtime in Deno[#](#use-at-runtime-in-deno)

You can use supabase-js in the Deno runtime via [JSR](https://jsr.io/@supabase/supabase-js)
:

`     _10  import { createClient } from 'jsr:@supabase/supabase-js@2'      `

* * *

Initializing
------------

Create a new client for use in the browser.

You can initialize a new Supabase client using the `createClient()` method.

The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything we offer within the Supabase ecosystem.

### Parameters

*   supabaseUrlRequiredstring
    
    The unique Supabase URL which is supplied when you create a new project in your project dashboard.
    
*   supabaseKeyRequiredstring
    
    The unique Supabase Key which is supplied when you create a new project in your project dashboard.
    
*   optionsOptionalSupabaseClientOptions
    
    Details
    

Creating a clientWith a custom domainWith additional parametersWith custom schemasCustom fetch implementationReact Native options with AsyncStorageReact Native options with Expo SecureStore

`     _10  import { createClient } from '@supabase/supabase-js'  _10  _10  // Create a single supabase client for interacting with your database  _10  const supabase = createClient('https://xyzcompany.supabase.co', 'public-anon-key')      `

* * *

TypeScript support
------------------

`supabase-js` has TypeScript support for type inference, autocompletion, type-safe queries, and more.

With TypeScript, `supabase-js` detects things like `not null` constraints and [generated columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html)
. Nullable columns are typed as `T | null` when you select the column. Generated columns will show a type error when you insert to it.

`supabase-js` also detects relationships between tables. A referenced table with one-to-many relationship is typed as `T[]`. Likewise, a referenced table with many-to-one relationship is typed as `T | null`.

Generating TypeScript Types[#](#generating-typescript-types)

-------------------------------------------------------------

You can use the Supabase CLI to [generate the types](/docs/reference/cli/supabase-gen-types)
. You can also generate the types [from the dashboard](https://supabase.com/dashboard/project/_/api?page=tables-intro)
.

Terminal

`     _10  supabase gen types typescript --project-id abcdefghijklmnopqrst > database.types.ts      `

These types are generated from your database schema. Given a table `public.movies`, the generated types will look like:

`     _10  create table public.movies (  _10  id bigint generated always as identity primary key,  _10  name text not null,  _10  data jsonb null  _10  );      `

./database.types.ts

``     _25  export type Json = string | number | boolean | null | { [key: string]: Json | undefined } | Json[]  _25  _25  export interface Database {  _25  public: {  _25  Tables: {  _25  movies: {  _25  Row: { // the data expected from .select()  _25  id: number  _25  name: string  _25  data: Json | null  _25  }  _25  Insert: { // the data to be passed to .insert()  _25  id?: never // generated columns must not be supplied  _25  name: string // `not null` columns with no default must be supplied  _25  data?: Json | null // nullable columns can be omitted  _25  }  _25  Update: { // the data to be passed to .update()  _25  id?: never  _25  name?: string // `not null` columns are optional on .update()  _25  data?: Json | null  _25  }  _25  }  _25  }  _25  }  _25  }      ``

Using TypeScript type definitions[#](#using-typescript-type-definitions)

-------------------------------------------------------------------------

You can supply the type definitions to `supabase-js` like so:

./index.tsx

`     _10  import { createClient } from '@supabase/supabase-js'  _10  import { Database } from './database.types'  _10  _10  const supabase = createClient<Database>(  _10  process.env.SUPABASE_URL,  _10  process.env.SUPABASE_ANON_KEY  _10  )      `

Helper types for Tables and Joins[#](#helper-types-for-tables-and-joins)

-------------------------------------------------------------------------

You can use the following helper types to make the generated TypeScript types easier to use.

Sometimes the generated types are not what you expect. For example, a view's column may show up as nullable when you expect it to be `not null`. Using [type-fest](https://github.com/sindresorhus/type-fest)
, you can override the types like so:

./database-generated.types.ts

`     _10  export type Json = // ...  _10  _10  export interface Database {  _10  // ...  _10  }      `

./database.types.ts

``     _20  import { MergeDeep } from 'type-fest'  _20  import { Database as DatabaseGenerated } from './database-generated.types'  _20  export { Json } from './database-generated.types'  _20  _20  // Override the type for a specific column in a view:  _20  export type Database = MergeDeep<  _20  DatabaseGenerated,  _20  {  _20  public: {  _20  Views: {  _20  movies_view: {  _20  Row: {  _20  // id is a primary key in public.movies, so it must be `not null`  _20  id: number  _20  }  _20  }  _20  }  _20  }  _20  }  _20  >      ``

You can also override the type of an individual successful response if needed:

`     _10  const { data } = await supabase.from('countries').select().returns<MyType>()      `

The generated types provide shorthands for accessing tables and enums.

./index.ts

`     _10  import { Database, Tables, Enums } from "./database.types.ts";  _10  _10  // Before 😕  _10  let movie: Database['public']['Tables']['movies']['Row'] = // ...  _10  _10  // After 😍  _10  let movie: Tables<'movies'>      `

### Response types for complex queries[#](#response-types-for-complex-queries)

`supabase-js` always returns a `data` object (for success), and an `error` object (for unsuccessful requests).

These helper types provide the result types from any query, including nested types for database joins.

Given the following schema with a relation between cities and countries, we can get the nested `CountriesWithCities` type:

`     _10  create table countries (  _10  "id" serial primary key,  _10  "name" text  _10  );  _10  _10  create table cities (  _10  "id" serial primary key,  _10  "name" text,  _10  "country_id" int references "countries"  _10  );      `

``     _17  import { QueryResult, QueryData, QueryError } from '@supabase/supabase-js'  _17  _17  const countriesWithCitiesQuery = supabase  _17  .from("countries")  _17  .select(`  _17  id,  _17  name,  _17  cities (  _17  id,  _17  name  _17  )  _17  `);  _17  type CountriesWithCities = QueryData<typeof countriesWithCitiesQuery>;  _17  _17  const { data, error } = await countriesWithCitiesQuery;  _17  if (error) throw error;  _17  const countriesWithCities: CountriesWithCities = data;      ``

* * *

Fetch data
----------

Perform a SELECT query on the table or view.

*   By default, Supabase projects return a maximum of 1,000 rows. This setting can be changed in your project's [API settings](/dashboard/project/_/settings/api)
    . It's recommended that you keep it low to limit the payload size of accidental or malicious requests. You can use `range()` queries to paginate through your data.
*   `select()` can be combined with [Filters](/docs/reference/javascript/using-filters)
    
*   `select()` can be combined with [Modifiers](/docs/reference/javascript/using-modifiers)
    
*   `apikey` is a reserved keyword if you're using the [Supabase Platform](/docs/guides/platform)
     and [should be avoided as a column name](https://github.com/supabase/supabase/issues/5465)
    .

### Parameters

*   columnsOptionalQuery
    
    The columns to retrieve, separated by commas. Columns can be renamed when returned with `customName:columnName`
    
*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Getting your dataSelecting specific columnsQuery referenced tablesQuery referenced tables through a join tableQuery the same referenced table multiple timesFiltering through referenced tablesQuerying referenced table with countQuerying with count optionQuerying JSON dataQuerying referenced table with inner joinSwitching schemas per query

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()      `

Data source

Response

* * *

Insert data
-----------

Perform an INSERT into the table or view.

### Parameters

*   valuesRequiredUnion: expand to see options
    
    The values to insert. Pass an object to insert a single row or an array to insert multiple rows.
    
    Details
    
*   optionsOptionalobject
    
    Named parameters
    
    Details
    

Create a recordCreate a record and return itBulk create

`     _10  const { error } = await supabase  _10  .from('countries')  _10  .insert({ id: 1, name: 'Denmark' })      `

Data source

Response

* * *

Update data
-----------

Perform an UPDATE on the table or view.

*   `update()` should always be combined with [Filters](/docs/reference/javascript/using-filters)
     to target the item(s) you wish to update.

### Parameters

*   valuesRequiredRow
    
    The values to update with
    
*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Updating your dataUpdate a record and return itUpdating JSON data

`     _10  const { error } = await supabase  _10  .from('countries')  _10  .update({ name: 'Australia' })  _10  .eq('id', 1)      `

Data source

Response

* * *

Upsert data
-----------

Perform an UPSERT on the table or view. Depending on the column(s) passed to `onConflict`, `.upsert()` allows you to perform the equivalent of `.insert()` if a row with the corresponding `onConflict` columns doesn't exist, or if it does exist, perform an alternative action depending on `ignoreDuplicates`.

*   Primary keys must be included in `values` to use upsert.

### Parameters

*   valuesRequiredUnion: expand to see options
    
    The values to upsert with. Pass an object to upsert a single row or an array to upsert multiple rows.
    
    Details
    
*   optionsOptionalobject
    
    Named parameters
    
    Details
    

Upsert your dataBulk Upsert your dataUpserting into tables with constraints

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .upsert({ id: 1, name: 'Albania' })  _10  .select()      `

Data source

Response

* * *

Delete data
-----------

Perform a DELETE on the table or view.

*   `delete()` should always be combined with [filters](/docs/reference/javascript/using-filters)
     to target the item(s) you wish to delete.
*   If you use `delete()` with filters and you have [RLS](/docs/learn/auth-deep-dive/auth-row-level-security)
     enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/`ALL` policy that makes the rows visible.
*   When using `delete().in()`, specify an array of values to target multiple rows with a single query. This is particularly useful for batch deleting entries that share common criteria, such as deleting users by their IDs. Ensure that the array you provide accurately represents all records you intend to delete to avoid unintended data removal.

### Parameters

*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Delete a single recordDelete a record and return itDelete multiple records

`     _10  const response = await supabase  _10  .from('countries')  _10  .delete()  _10  .eq('id', 1)      `

Data source

Response

* * *

Call a Postgres function
------------------------

Perform a function call.

You can call Postgres functions as _Remote Procedure Calls_, logic in your database that you can execute from anywhere. Functions are useful when the logic rarely changes—like for password resets and updates.

`     _10  create or replace function hello_world() returns text as $$  _10  select 'Hello world';  _10  $$ language sql;      `

To call Postgres functions on [Read Replicas](/docs/guides/platform/read-replicas)
, use the `get: true` option.

### Parameters

*   fnRequiredFnName
    
    The function name to call
    
*   argsRequiredFn\['Args'\]
    
    The arguments to pass to the function call
    
*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Call a Postgres function without argumentsCall a Postgres function with argumentsBulk processingCall a Postgres function with filtersCall a read-only Postgres function

`     _10  const { data, error } = await supabase.rpc('hello_world')      `

Data source

Response

* * *

Using filters
-------------

Filters allow you to only return rows that match certain conditions.

Filters can be used on `select()`, `update()`, `upsert()`, and `delete()` queries.

If a Postgres function returns a table response, you can also apply filters.

Applying FiltersChainingConditional ChainingFilter by values within a JSON columnFilter referenced tables

`     _10  const { data, error } = await supabase  _10  .from('cities')  _10  .select('name, country_id')  _10  .eq('name', 'The Shire') // Correct  _10  _10  const { data, error } = await supabase  _10  .from('cities')  _10  .eq('name', 'The Shire') // Incorrect  _10  .select('name, country_id')      `

Notes

* * *

Column is equal to a value
--------------------------

Match only rows where `column` is equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredNonNullable
    
    The value to filter with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .eq('name', 'Albania')      `

Data source

Response

* * *

Column is not equal to a value
------------------------------

Match only rows where `column` is not equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .neq('name', 'Albania')      `

Data source

Response

* * *

Column is greater than a value
------------------------------

Match only rows where `column` is greater than `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .gt('id', 2)      `

Data source

Response

Notes

* * *

Column is greater than or equal to a value
------------------------------------------

Match only rows where `column` is greater than or equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .gte('id', 2)      `

Data source

Response

* * *

Column is less than a value
---------------------------

Match only rows where `column` is less than `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .lt('id', 2)      `

Data source

Response

* * *

Column is less than or equal to a value
---------------------------------------

Match only rows where `column` is less than or equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .lte('id', 2)      `

Data source

Response

* * *

Column matches a pattern
------------------------

Match only rows where `column` matches `pattern` case-sensitively.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   patternRequiredstring
    
    The pattern to match with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .like('name', '%Alba%')      `

Data source

Response

* * *

Column matches a case-insensitive pattern
-----------------------------------------

Match only rows where `column` matches `pattern` case-insensitively.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   patternRequiredstring
    
    The pattern to match with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .ilike('name', '%alba%')      `

Data source

Response

* * *

Column is a value
-----------------

Match only rows where `column` IS `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

Checking for nullness, true or false

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .is('name', null)      `

Data source

Response

Notes

* * *

Column is in an array
---------------------

Match only rows where `column` is included in the `values` array.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valuesRequiredArray<Row\['ColumnName'\]>
    
    The values array to filter with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .in('name', ['Albania', 'Algeria'])      `

Data source

Response

* * *

Column contains every element in a value
----------------------------------------

Only relevant for jsonb, array, and range columns. Match only rows where `column` contains every element appearing in `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The jsonb, array, or range column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The jsonb, array, or range value to filter with
    
    Details
    

On array columnsOn range columnsOn \`jsonb\` columns

`     _10  const { data, error } = await supabase  _10  .from('issues')  _10  .select()  _10  .contains('tags', ['is:open', 'priority:low'])      `

Data source

Response

* * *

Contained by value
------------------

Only relevant for jsonb, array, and range columns. Match only rows where every element appearing in `column` is contained by `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The jsonb, array, or range column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The jsonb, array, or range value to filter with
    
    Details
    

On array columnsOn range columnsOn \`jsonb\` columns

`     _10  const { data, error } = await supabase  _10  .from('classes')  _10  .select('name')  _10  .containedBy('days', ['monday', 'tuesday', 'wednesday', 'friday'])      `

Data source

Response

* * *

Greater than a range
--------------------

Only relevant for range columns. Match only rows where every element in `column` is greater than any element in `range`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The range column to filter on
    
    Details
    
*   rangeRequiredstring
    
    The range to filter with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeGt('during', '[2000-01-02 08:00, 2000-01-02 09:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Greater than or equal to a range\
--------------------------------\
\
Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or greater than any element in `range`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeGte('during', '[2000-01-02 08:30, 2000-01-02 09:30)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Less than a range\
-----------------\
\
Only relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeLt('during', '[2000-01-01 15:00, 2000-01-01 16:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Less than or equal to a range\
-----------------------------\
\
Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or less than any element in `range`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeLte('during', '[2000-01-01 14:00, 2000-01-01 16:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Mutually exclusive to a range\
-----------------------------\
\
Only relevant for range columns. Match only rows where `column` is mutually exclusive to `range` and there can be no element between the two ranges.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeAdjacent('during', '[2000-01-01 12:00, 2000-01-01 13:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
With a common element\
---------------------\
\
Only relevant for array and range columns. Match only rows where `column` and `value` have an element in common.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The array or range column to filter on\
    \
    Details\
    \
*   valueRequiredUnion: expand to see options\
    \
    The array or range value to filter with\
    \
    Details\
    \
\
On array columnsOn range columns\
\
`     _10  const { data, error } = await supabase  _10  .from('issues')  _10  .select('title')  _10  .overlaps('tags', ['is:closed', 'severity:high'])      `\
\
Data source\
\
Response\
\
* * *\
\
Match a string\
--------------\
\
Only relevant for text and tsvector columns. Match only rows where `column` matches the query string in `query`.\
\
*   For more information, see [Postgres full text search](/docs/guides/database/full-text-search)\
    .\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The text or tsvector column to filter on\
    \
    Details\
    \
*   queryRequiredstring\
    \
    The query text to match with\
    \
*   optionsOptionalobject\
    \
    Named parameters\
    \
    Details\
    \
\
Text searchBasic normalizationFull normalizationWebsearch\
\
``     _10  const result = await supabase  _10  .from("texts")  _10  .select("content")  _10  .textSearch("content", `'eggs' & 'ham'`, {  _10  config: "english",  _10  });      ``\
\
Data source\
\
Response\
\
* * *\
\
Match an associated value\
-------------------------\
\
Match only rows where each column in `query` keys is equal to its associated value. Shorthand for multiple `.eq()`s.\
\
### Parameters\
\
*   queryRequiredUnion: expand to see options\
    \
    The object to filter with, with column names as keys mapped to their filter values\
    \
    Details\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .match({ id: 2, name: 'Albania' })      `\
\
Data source\
\
Response\
\
* * *\
\
Don't match the filter\
----------------------\
\
Match only rows which doesn't satisfy the filter.\
\
not() expects you to use the raw PostgREST syntax for the filter values.\
\
``     _10  .not('id', 'in', '(5,6,7)') // Use `()` for `in` filter  _10  .not('arraycol', 'cs', '\{"a","b"\}') // Use `cs` for `contains()`, `\{\}` for array values      ``\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The column to filter on\
    \
    Details\
    \
*   operatorRequiredUnion: expand to see options\
    \
    The operator to be negated to filter with, following PostgREST syntax\
    \
    Details\
    \
*   valueRequiredUnion: expand to see options\
    \
    The value to filter with, following PostgREST syntax\
    \
    Details\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .not('name', 'is', null)      `\
\
Data source\
\
Response\
\
* * *\
\
Match at least one filter\
-------------------------\
\
Match only rows which satisfy at least one of the filters.\
\
or() expects you to use the raw PostgREST syntax for the filter names and values.\
\
``     _10  .or('id.in.(5,6,7), arraycol.cs.\{"a","b"\}') // Use `()` for `in` filter, `\{\}` for array values and `cs` for `contains()`.  _10  .or('id.in.(5,6,7), arraycol.cd.\{"a","b"\}') // Use `cd` for `containedBy()`      ``\
\
### Parameters\
\
*   filtersRequiredstring\
    \
    The filters to use, following PostgREST syntax\
    \
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`Use \`or\` with \`and\`Use \`or\` on referenced tables\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .or('id.eq.2,name.eq.Algeria')      `\
\
Data source\
\
Response\
\
* * *\
\
Match the filter\
----------------\
\
Match only rows which satisfy the filter. This is an escape hatch - you should use the specific filter methods wherever possible.\
\
filter() expects you to use the raw PostgREST syntax for the filter values.\
\
``     _10  .filter('id', 'in', '(5,6,7)') // Use `()` for `in` filter  _10  .filter('arraycol', 'cs', '\{"a","b"\}') // Use `cs` for `contains()`, `\{\}` for array values      ``\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The column to filter on\
    \
    Details\
    \
*   operatorRequiredUnion: expand to see options\
    \
    The operator to filter with, following PostgREST syntax\
    \
    Details\
    \
*   valueRequiredunknown\
    \
    The value to filter with, following PostgREST syntax\
    \
\
With \`select()\`On a referenced table\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .filter('name', 'in', '("Algeria","Japan")')      `\
\
Data source\
\
Response\
\
* * *\
\
Using modifiers\
---------------\
\
Filters work on the row level—they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition—allowing you to change the format of the response (e.g., returning a CSV string).\
\
Modifiers must be specified after filters. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).\
\
* * *\
\
Return data after inserting\
---------------------------\
\
Perform a SELECT on the query result.\
\
### Parameters\
\
*   columnsOptionalQuery\
    \
    The columns to retrieve, separated by commas\
    \
\
With \`upsert()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .upsert({ id: 1, name: 'Algeria' })  _10  .select()      `\
\
Data source\
\
Response\
\
* * *\
\
Order the results\
-----------------\
\
Order the query result by `column`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The column to order by\
    \
    Details\
    \
*   optionsOptionalobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`On a referenced table\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('id', 'name')  _10  .order('id', { ascending: false })      `\
\
Data source\
\
Response\
\
* * *\
\
Limit the number of rows returned\
---------------------------------\
\
Limit the query result by `count`.\
\
### Parameters\
\
*   countRequirednumber\
    \
    The maximum number of rows to return\
    \
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`On a referenced table\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .limit(1)      `\
\
Data source\
\
Response\
\
* * *\
\
Limit the query to a range\
--------------------------\
\
Limit the query result by starting at an offset (`from`) and ending at the offset (`from + to`). Only records within this range are returned. This respects the query order and if there is no order clause the range could behave unexpectedly. The `from` and `to` values are 0-based and inclusive: `range(1, 3)` will include the second, third and fourth rows of the query.\
\
### Parameters\
\
*   fromRequirednumber\
    \
    The starting index from which to limit the result\
    \
*   toRequirednumber\
    \
    The last index to which to limit the result\
    \
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .range(0, 1)      `\
\
Data source\
\
Response\
\
* * *\
\
Set an abort signal\
-------------------\
\
Set the AbortSignal for the fetch request.\
\
You can use this to set a timeout for the request.\
\
### Parameters\
\
*   signalRequiredAbortSignal\
    \
    The AbortSignal to use for the fetch request\
    \
\
Aborting requests in-flightSet a timeout\
\
`     _10  const ac = new AbortController()  _10  ac.abort()  _10  const { data, error } = await supabase  _10  .from('very_big_table')  _10  .select()  _10  .abortSignal(ac.signal)      `\
\
Response\
\
Notes\
\
* * *\
\
Retrieve one row of data\
------------------------\
\
Return `data` as a single object instead of an array of objects.\
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .limit(1)  _10  .single()      `\
\
Data source\
\
Response\
\
* * *\
\
Retrieve zero or one row of data\
--------------------------------\
\
Return `data` as a single object instead of an array of objects.\
\
### Return Type\
\
Union: expand to see options\
\
Details\
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .eq('name', 'Singapore')  _10  .maybeSingle()      `\
\
Data source\
\
Response\
\
* * *\
\
Retrieve as a CSV\
-----------------\
\
Return `data` as a string in CSV format.\
\
### Return Type\
\
string\
\
Return data as CSV\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .csv()      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Override type of successful response\
------------------------------------\
\
Override the type of the returned `data`.\
\
Override type of successful response\
\
`     _10  const { data } = await supabase  _10  .from('countries')  _10  .select()  _10  .returns<MyType>()      `\
\
Response\
\
* * *\
\
Using explain\
-------------\
\
Return `data` as the EXPLAIN plan for the query.\
\
For debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html)\
 of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.\
\
Explain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.\
\
Follow the [Performance Debugging Guide](/docs/guides/database/debugging-performance)\
 to enable the functionality on your project.\
\
### Parameters\
\
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
### Return Type\
\
Union: expand to see options\
\
Details\
\
Get the execution planGet the execution plan with analyze and verbose\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .explain()      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Overview\
--------\
\
*   The auth methods can be accessed via the `supabase.auth` namespace.\
    \
*   By default, the supabase client sets `persistSession` to true and attempts to store the session in local storage. When using the supabase client in an environment that doesn't support local storage, you might notice the following warning message being logged:\
    \
    > No storage option exists to persist the session, which may result in unexpected behavior when using auth. If you want to set `persistSession` to true, please provide a storage option or you may set `persistSession` to false to disable this warning.\
    \
    This warning message can be safely ignored if you're not using auth on the server-side. If you are using auth and you want to set `persistSession` to true, you will need to provide a custom storage implementation that follows [this interface](https://github.com/supabase/gotrue-js/blob/master/src/lib/types.ts#L1027)\
    .\
    \
*   Any email links and one-time passwords (OTPs) sent have a default expiry of 24 hours. We have the following [rate limits](/docs/guides/platform/going-into-prod#auth-rate-limits)\
     in place to guard against brute force attacks.\
    \
*   The expiry of an access token can be set in the "JWT expiry limit" field in [your project's auth settings](/dashboard/project/_/settings/auth)\
    . A refresh token never expires and can only be used once.\
    \
\
Create auth clientCreate auth client (server-side)\
\
`     _10  import { createClient } from '@supabase/supabase-js'  _10  _10  const supabase = createClient(supabase_url, anon_key)      `\
\
* * *\
\
Error codes\
-----------\
\
Supabase Auth can throw or return various errors when using the API. All errors originating from the `supabase.auth` namespace of the client library will be wrapped by the `AuthError` class.\
\
Error objects are split in a few classes:\
\
*   `AuthApiError` -- errors which originate from the Supabase Auth API.\
    *   Use `isAuthApiError` instead of `instanceof` checks to see if an error you caught is of this type.\
*   `CustomAuthError` -- errors which generally originate from state in the client library.\
    *   Use the `name` property on the error to identify the class of error received.\
\
Errors originating from the server API classed as `AuthApiError` always have a `code` property that can be used to identify the error returned by the server. The `status` property is also present, encoding the HTTP status code received in the response.\
\
In general the HTTP status codes you will likely receive are:\
\
*   [403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403)\
     is sent out in rare situations where a certain Auth feature is not available for the user, and you as the developer are not checking a precondition whether that API is available for the user.\
*   [422 Unprocessable Entity](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422)\
     is sent out when the API request is accepted, but cannot be processed because the user or Auth server is in a state where it cannot satisfy the request.\
*   [429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)\
     is sent out when rate-limits are breached for an API. You should handle this status code often, especially in functions that authenticate a user.\
*   [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)\
     often means that the Auth server's service is degraded. Most often it points to issues in your database setup such as a misbehaving trigger on a schema, function, view or other database object.\
*   [501 Not Implemented](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501)\
     is sent out when a feature is not enabled on the Auth server, and you are trying to use an API which requires it.\
\
To supplement HTTP status codes, Supabase Auth returns a string error code which gives you more insight into what went wrong. These codes are stable and can be used to present an internationalized message to your users.\
\
| Code | Description |\
| --- | --- |\
| `anonymous_provider_disabled` | Anonymous sign-ins are disabled. |\
| `bad_code_verifier` | Returned from the PKCE flow where the provided code verifier does not match the expected one. Indicates a bug in the implementation of the client library. |\
| `bad_json` | Usually used when the HTTP body of the request is not valid JSON. |\
| `bad_jwt` | JWT sent in the `Authorization` header is not valid. |\
| `bad_oauth_callback` | OAuth callback from provider to Auth does not have all the required attributes (state). Indicates an issue with the OAuth provider or client library implementation. |\
| `bad_oauth_state` | OAuth state (data echoed back by the OAuth provider to Supabase Auth) is not in the correct format. Indicates an issue with the OAuth provider integration. |\
| `captcha_failed` | Captcha challenge could not be verified with the captcha provider. Check your captcha integration. |\
| `conflict` | General database conflict, such as concurrent requests on resources that should not be modified concurrently. Can often occur when you have too many session refresh requests firing off at the same time for a user. Check your app for concurrency issues, and if detected, back off exponentially. |\
| `email_conflict_identity_not_deletable` | Unlinking this identity causes the user's account to change to an email address which is already used by another user account. Indicates an issue where the user has two different accounts using different primary email addresses. You may need to migrate user data to one of their accounts in this case. |\
| `email_exists` | Email address already exists in the system. |\
| `email_not_confirmed` | Signing in is not allowed for this user as the email address is not confirmed. |\
| `email_provider_disabled` | Signups are disabled for email and password. |\
| `flow_state_expired` | PKCE flow state to which the API request relates has expired. Ask the user to sign in again. |\
| `flow_state_not_found` | PKCE flow state to which the API request relates no longer exists. Flow states expire after a while and are progressively cleaned up, which can cause this error. Retried requests can cause this error, as the previous request likely destroyed the flow state. Ask the user to sign in again. |\
| `hook_payload_over_size_limit` | Payload from Auth exceeds maximum size limit. |\
| `hook_timeout` | Unable to reach hook within maximum time allocated. |\
| `hook_timeout_after_retry` | Unable to reach hook after maximum number of retries. |\
| `identity_already_exists` | The identity to which the API relates is already linked to a user. |\
| `identity_not_found` | Identity to which the API call relates does not exist, such as when an identity is unlinked or deleted. |\
| `insufficient_aal` | To call this API, the user must have a higher [Authenticator Assurance Level](https://supabase.com/docs/guides/auth/auth-mfa)<br>. To resolve, ask the user to solve an MFA challenge. |\
| `invite_not_found` | Invite is expired or already used. |\
| `invalid_credentials` | Login credentials or grant type not recognized. |\
| `manual_linking_disabled` | Calling the `supabase.auth.linkUser()` and related APIs is not enabled on the Auth server. |\
| `mfa_challenge_expired` | Responding to an MFA challenge should happen within a fixed time period. Request a new challenge when encountering this error. |\
| `mfa_factor_name_conflict` | MFA factors for a single user should not have the same friendly name. |\
| `mfa_factor_not_found` | MFA factor no longer exists. |\
| `mfa_ip_address_mismatch` | The enrollment process for MFA factors must begin and end with the same IP address. |\
| `mfa_verification_failed` | MFA challenge could not be verified -- wrong TOTP code. |\
| `mfa_verification_rejected` | Further MFA verification is rejected. Only returned if the [MFA verification attempt hook](https://supabase.com/docs/guides/auth/auth-hooks?language=add-admin-role#hook-mfa-verification-attempt)<br> returns a reject decision. |\
| `mfa_verified_factor_exists` | Verified phone factor already exists for a user. Unenroll existing verified phone factor to continue. |\
| `mfa_totp_enroll_disabled` | Enrollment of MFA TOTP factors is disabled. |\
| `mfa_totp_verify_disabled` | Login via TOTP factors and verification of new TOTP factors is disabled. |\
| `mfa_phone_enroll_disabled` | Enrollment of MFA Phone factors is disabled. |\
| `mfa_phone_verify_disabled` | Login via Phone factors and verification of new Phone factors is disabled. |\
| `no_authorization` | This HTTP request requires an `Authorization` header, which is not provided. |\
| `not_admin` | User accessing the API is not admin, i.e. the JWT does not contain a `role` claim that identifies them as an admin of the Auth server. |\
| `oauth_provider_not_supported` | Using an OAuth provider which is disabled on the Auth server. |\
| `otp_disabled` | Sign in with OTPs (magic link, email OTP) is disabled. Check your sever's configuration. |\
| `otp_expired` | OTP code for this sign-in has expired. Ask the user to sign in again. |\
| `over_email_send_rate_limit` | Too many emails have been sent to this email address. Ask the user to wait a while before trying again. |\
| `over_request_rate_limit` | Too many requests have been sent by this client (IP address). Ask the user to try again in a few minutes. Sometimes can indicate a bug in your application that mistakenly sends out too many requests (such as a badly written [`useEffect` React hook](https://react.dev/reference/react/useEffect)<br>). |\
| `over_sms_send_rate_limit` | Too many SMS messages have been sent to this phone number. Ask the user to wait a while before trying again. |\
| `phone_exists` | Phone number already exists in the system. |\
| `phone_not_confirmed` | Signing in is not allowed for this user as the phone number is not confirmed. |\
| `phone_provider_disabled` | Signups are disabled for phone and password. |\
| `provider_disabled` | OAuth provider is disabled for use. Check your server's configuration. |\
| `provider_email_needs_verification` | Not all OAuth providers verify their user's email address. Supabase Auth requires emails to be verified, so this error is sent out when a verification email is sent after completing the OAuth flow. |\
| `reauthentication_needed` | A user needs to reauthenticate to change their password. Ask the user to reauthenticate by calling the `supabase.auth.reauthenticate()` API. |\
| `reauthentication_not_valid` | Verifying a reauthentication failed, the code is incorrect. Ask the user to enter a new code. |\
| `request_timeout` | Processing the request took too long. Retry the request. |\
| `same_password` | A user that is updating their password must use a different password than the one currently used. |\
| `saml_assertion_no_email` | SAML assertion (user information) was received after sign in, but no email address was found in it, which is required. Check the provider's attribute mapping and/or configuration. |\
| `saml_assertion_no_user_id` | SAML assertion (user information) was received after sign in, but a user ID (called NameID) was not found in it, which is required. Check the SAML identity provider's configuration. |\
| `saml_entity_id_mismatch` | (Admin API.) Updating the SAML metadata for a SAML identity provider is not possible, as the entity ID in the update does not match the entity ID in the database. This is equivalent to creating a new identity provider, and you should do that instead. |\
| `saml_idp_already_exists` | (Admin API.) Adding a SAML identity provider that is already added. |\
| `saml_idp_not_found` | SAML identity provider not found. Most often returned after IdP-initiated sign-in with an unregistered SAML identity provider in Supabase Auth. |\
| `saml_metadata_fetch_failed` | (Admin API.) Adding or updating a SAML provider failed as its metadata could not be fetched from the provided URL. |\
| `saml_provider_disabled` | Using [Enterprise SSO with SAML 2.0](https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml)<br> is not enabled on the Auth server. |\
| `saml_relay_state_expired` | SAML relay state is an object that tracks the progress of a `supabase.auth.signInWithSSO()` request. The SAML identity provider should respond after a fixed amount of time, after which this error is shown. Ask the user to sign in again. |\
| `saml_relay_state_not_found` | SAML relay states are progressively cleaned up after they expire, which can cause this error. Ask the user to sign in again. |\
| `session_not_found` | Session to which the API request relates no longer exists. This can occur if the user has signed out, or the session entry in the database was deleted in some other way. |\
| `signup_disabled` | Sign ups (new account creation) are disabled on the server. |\
| `single_identity_not_deletable` | Every user must have at least one identity attached to it, so deleting (unlinking) an identity is not allowed if it's the only one for the user. |\
| `sms_send_failed` | Sending an SMS message failed. Check your SMS provider configuration. |\
| `sso_domain_already_exists` | (Admin API.) Only one SSO domain can be registered per SSO identity provider. |\
| `sso_provider_not_found` | SSO provider not found. Check the arguments in `supabase.auth.signInWithSSO()`. |\
| `too_many_enrolled_mfa_factors` | A user can only have a fixed number of enrolled MFA factors. |\
| `unexpected_audience` | (Deprecated feature not available via Supabase client libraries.) The request's `X-JWT-AUD` claim does not match the JWT's audience. |\
| `unexpected_failure` | Auth service is degraded or a bug is present, without a specific reason. |\
| `user_already_exists` | User with this information (email address, phone number) cannot be created again as it already exists. |\
| `user_banned` | User to which the API request relates has a `banned_until` property which is still active. No further API requests should be attempted until this field is cleared. |\
| `user_not_found` | User to which the API request relates no longer exists. |\
| `user_sso_managed` | When a user comes from SSO, certain fields of the user cannot be updated (like `email`). |\
| `validation_failed` | Provided parameters are not in the expected format. |\
| `weak_password` | User is signing up or changing their password without meeting the password strength criteria. Use the `AuthWeakPasswordError` class to access more information about what they need to do to make the password pass. |\
\
### Tips for better error handling[#](#tips-for-better-error-handling)\
\
*   Do not use string matching on error messages! Always use the `name` and `code` properties of error objects to identify the situation.\
*   Although HTTP status codes generally don't change, they can suddenly change due to bugs, so avoid relying on them unless absolutely necessary.\
\
* * *\
\
Create a new user\
-----------------\
\
Creates a new user.\
\
*   By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](/dashboard/project/_/auth/providers)\
    .\
*   **Confirm email** determines if users need to confirm their email address after signing up.\
    *   If **Confirm email** is enabled, a `user` is returned but `session` is null.\
    *   If **Confirm email** is disabled, both a `user` and a `session` are returned.\
*   When the user confirms their email address, they are redirected to the [`SITE_URL`](/docs/guides/auth/redirect-urls)\
     by default. You can modify your `SITE_URL` or add additional redirect URLs in [your project](/dashboard/project/_/auth/url-configuration)\
    .\
*   If signUp() is called for an existing confirmed user:\
    *   When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](/dashboard/project/_/auth/providers)\
        , an obfuscated/fake user object is returned.\
    *   When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.\
*   To fetch the currently logged-in user, refer to [`getUser()`](/docs/reference/javascript/auth-getuser)\
    .\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign up with an email and passwordSign up with a phone number and password (SMS)Sign up with a phone number and password (whatsapp)Sign up with additional user metadataSign up with a redirect URL\
\
`     _10  const { data, error } = await supabase.auth.signUp({  _10  email: 'example@email.com',  _10  password: 'example-password',  _10  })      `\
\
Response\
\
* * *\
\
Listen to auth events\
---------------------\
\
Receive a notification every time an auth event happens.\
\
*   Subscribes to important events occurring on the user's session.\
*   Use on the frontend/client. It is less useful on the server.\
*   Events are emitted across tabs to keep your application's UI up-to-date. Some events can fire very frequently, based on the number of tabs open. Use a quick and efficient callback function, and defer or debounce as many operations as you can to be performed outside of the callback.\
*   **Important:** A callback can be an `async` function and it runs synchronously during the processing of the changes causing the event. You can easily create a dead-lock by using `await` on a call to another method of the Supabase library.\
    *   Avoid using `async` functions as callbacks.\
    *   Limit the number of `await` calls in `async` callbacks.\
    *   Do not use other Supabase functions in the callback function. If you must, dispatch the functions once the callback has finished executing. Use this as a quick way to achieve this:\
        \
        `     _10  supabase.auth.onAuthStateChange((event, session) => \{  _10  setTimeout(async () => \{  _10  // await on other Supabase function here  _10  // this runs right after the callback has finished  _10  \}, 0)  _10  \})      `\
        \
*   Emitted events:\
    *   `INITIAL_SESSION`\
        *   Emitted right after the Supabase client is constructed and the initial session from storage is loaded.\
    *   `SIGNED_IN`\
        *   Emitted each time a user session is confirmed or re-established, including on user sign in and when refocusing a tab.\
        *   Avoid making assumptions as to when this event is fired, this may occur even when the user is already signed in. Instead, check the user object attached to the event to see if a new user has signed in and update your application's UI.\
        *   This event can fire very frequently depending on the number of tabs open in your application.\
    *   `SIGNED_OUT`\
        *   Emitted when the user signs out. This can be after:\
            *   A call to `supabase.auth.signOut()`.\
            *   After the user's session has expired for any reason:\
                *   User has signed out on another device.\
                *   The session has reached its timebox limit or inactivity timeout.\
                *   User has signed in on another device with single session per user enabled.\
                *   Check the [User Sessions](/docs/guides/auth/sessions)\
                     docs for more information.\
        *   Use this to clean up any local storage your application has associated with the user.\
    *   `TOKEN_REFRESHED`\
        *   Emitted each time a new access and refresh token are fetched for the signed in user.\
        *   It's best practice and highly recommended to extract the access token (JWT) and store it in memory for further use in your application.\
            *   Avoid frequent calls to `supabase.auth.getSession()` for the same purpose.\
        *   There is a background process that keeps track of when the session should be refreshed so you will always receive valid tokens by listening to this event.\
        *   The frequency of this event is related to the JWT expiry limit configured on your project.\
    *   `USER_UPDATED`\
        *   Emitted each time the `supabase.auth.updateUser()` method finishes successfully. Listen to it to update your application's UI based on new profile information.\
    *   `PASSWORD_RECOVERY`\
        *   Emitted instead of the `SIGNED_IN` event when the user lands on a page that includes a password recovery link in the URL.\
        *   Use it to show a UI to the user where they can [reset their password](/docs/guides/auth/passwords#resetting-a-users-password-forgot-password)\
            .\
\
### Parameters\
\
*   callbackRequiredfunction\
    \
    A callback function to be invoked when an auth event happens.\
    \
    Details\
    \
\
### Return Type\
\
object\
\
Details\
\
Listen to auth changesListen to sign outStore OAuth provider tokens on sign inUse React Context for the User's sessionListen to password recovery eventsListen to sign inListen to token refreshListen to user updates\
\
`     _20  const { data } = supabase.auth.onAuthStateChange((event, session) => {  _20  console.log(event, session)  _20  _20  if (event === 'INITIAL_SESSION') {  _20  // handle initial session  _20  } else if (event === 'SIGNED_IN') {  _20  // handle sign in event  _20  } else if (event === 'SIGNED_OUT') {  _20  // handle sign out event  _20  } else if (event === 'PASSWORD_RECOVERY') {  _20  // handle password recovery event  _20  } else if (event === 'TOKEN_REFRESHED') {  _20  // handle token refreshed event  _20  } else if (event === 'USER_UPDATED') {  _20  // handle user updated event  _20  }  _20  })  _20  _20  // call unsubscribe to remove the callback  _20  data.subscription.unsubscribe()      `\
\
* * *\
\
Create an anonymous user\
------------------------\
\
Creates a new anonymous user.\
\
*   Returns an anonymous user\
*   It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.\
\
### Parameters\
\
*   credentialsOptionalSignInAnonymouslyCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create an anonymous userCreate an anonymous user with custom user metadata\
\
`     _10  const { data, error } = await supabase.auth.signInAnonymously({  _10  options: {  _10  captchaToken  _10  }  _10  });      `\
\
Response\
\
* * *\
\
Sign in a user\
--------------\
\
Log in an existing user with an email and password or phone and password.\
\
*   Requires either an email and password or a phone number and password.\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in with email and passwordSign in with phone and password\
\
`     _10  const { data, error } = await supabase.auth.signInWithPassword({  _10  email: 'example@email.com',  _10  password: 'example-password',  _10  })      `\
\
Response\
\
* * *\
\
Sign in with ID Token\
---------------------\
\
Allows signing in with an OIDC ID token. The authentication provider used should be enabled and configured.\
\
### Parameters\
\
*   credentialsRequiredSignInWithIdTokenCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign In using ID Token\
\
`     _10  const { data, error } = await supabase.auth.signInWithIdToken({  _10  provider: 'google',  _10  token: 'your-id-token'  _10  })      `\
\
Response\
\
* * *\
\
Sign in a user through OTP\
--------------------------\
\
Log in a user using magiclink or a one-time password (OTP).\
\
*   Requires either an email or phone number.\
*   This method is used for passwordless sign-ins where a OTP is sent to the user's email or phone number.\
*   If the user doesn't exist, `signInWithOtp()` will signup the user instead. To restrict this behavior, you can set `shouldCreateUser` in `SignInWithPasswordlessCredentials.options` to `false`.\
*   If you're using an email, you can configure whether you want the user to receive a magiclink or a OTP.\
*   If you're using phone, you can configure whether you want the user to receive a OTP.\
*   The magic link's destination URL is determined by the [`SITE_URL`](/docs/guides/auth/redirect-urls)\
    .\
*   See [redirect URLs and wildcards](/docs/guides/auth#redirect-urls-and-wildcards)\
     to add additional redirect URLs to your project.\
*   Magic links and OTPs share the same implementation. To send users a one-time code instead of a magic link, [modify the magic link email template](/dashboard/project/_/auth/templates)\
     to include `\{\{ .Token \}\}` instead of `\{\{ .ConfirmationURL \}\}`.\
*   See our [Twilio Phone Auth Guide](/docs/guides/auth/phone-login?showSmsProvider=Twilio)\
     for details about configuring WhatsApp sign in.\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in with emailSign in with SMS OTPSign in with WhatsApp OTP\
\
`     _10  const { data, error } = await supabase.auth.signInWithOtp({  _10  email: 'example@email.com',  _10  options: {  _10  emailRedirectTo: 'https://example.com/welcome'  _10  }  _10  })      `\
\
Response\
\
Notes\
\
* * *\
\
Sign in a user through OAuth\
----------------------------\
\
Log in an existing user via a third-party provider. This method supports the PKCE flow.\
\
*   This method is used for signing in using a third-party provider.\
*   Supabase supports many different [third-party providers](/docs/guides/auth#configure-third-party-providers)\
    .\
\
### Parameters\
\
*   credentialsRequiredSignInWithOAuthCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in using a third-party providerSign in using a third-party provider with redirectSign in with scopes and access provider tokens\
\
`     _10  const { data, error } = await supabase.auth.signInWithOAuth({  _10  provider: 'github'  _10  })      `\
\
Response\
\
* * *\
\
Sign in a user through SSO\
--------------------------\
\
Attempts a single-sign on using an enterprise Identity Provider. A successful SSO attempt will redirect the current page to the identity provider authorization page. The redirect URL is implementation and SSO protocol specific.\
\
*   Before you can call this method you need to [establish a connection](/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections)\
     to an identity provider. Use the [CLI commands](/docs/reference/cli/supabase-sso)\
     to do this.\
*   If you've associated an email domain to the identity provider, you can use the `domain` property to start a sign-in flow.\
*   In case you need to use a different way to start the authentication flow with an identity provider, you can use the `providerId` property. For example:\
    *   Mapping specific user email addresses with an identity provider.\
    *   Using different hints to identity the identity provider to be used by the user, like a company-specific page, IP address or other tracking information.\
\
### Parameters\
\
*   paramsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in with email domainSign in with provider UUID\
\
`     _11  // You can extract the user's email domain and use it to trigger the  _11  // authentication flow with the correct identity provider.  _11  _11  const { data, error } = await supabase.auth.signInWithSSO({  _11  domain: 'company.com'  _11  })  _11  _11  if (data?.url) {  _11  // redirect the user to the identity provider's authentication flow  _11  window.location.href = data.url  _11  }      `\
\
* * *\
\
Sign out a user\
---------------\
\
Inside a browser context, `signOut()` will remove the logged in user from the browser session and log them out - removing all items from localstorage and then trigger a `"SIGNED_OUT"` event.\
\
*   In order to use the `signOut()` method, the user needs to be signed in first.\
*   By default, `signOut()` uses the global scope, which signs out all other sessions that the user is logged into as well.\
*   Since Supabase Auth uses JWTs for authentication, the access token JWT will be valid until it's expired. When the user signs out, Supabase revokes the refresh token and deletes the JWT from the client-side. This does not revoke the JWT and it will still be valid until it expires.\
\
### Parameters\
\
*   optionsRequiredSignOut\
    \
    Details\
    \
\
### Return Type\
\
Promise<object>\
\
Details\
\
Sign out\
\
`     _10  const { error } = await supabase.auth.signOut()      `\
\
* * *\
\
Send a password reset request\
-----------------------------\
\
Sends a password reset request to an email address. This method supports the PKCE flow.\
\
*   The password reset flow consist of 2 broad steps: (i) Allow the user to login via the password reset link; (ii) Update the user's password.\
*   The `resetPasswordForEmail()` only sends a password reset link to the user's email. To update the user's password, see [`updateUser()`](/docs/reference/javascript/auth-updateuser)\
    .\
*   A `SIGNED_IN` and `PASSWORD_RECOVERY` event will be emitted when the password recovery link is clicked. You can use [`onAuthStateChange()`](/docs/reference/javascript/auth-onauthstatechange)\
     to listen and invoke a callback function on these events.\
*   When the user clicks the reset link in the email they are redirected back to your application. You can configure the URL that the user is redirected to with the `redirectTo` parameter. See [redirect URLs and wildcards](/docs/guides/auth#redirect-urls-and-wildcards)\
     to add additional redirect URLs to your project.\
*   After the user has been redirected successfully, prompt them for a new password and call `updateUser()`:\
\
`     _10  const \{ data, error \} = await supabase.auth.updateUser(\{  _10  password: new_password  _10  \})      `\
\
### Parameters\
\
*   emailRequiredstring\
    \
    The email address of the user.\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Reset passwordReset password (React)\
\
`     _10  const { data, error } = await supabase.auth.resetPasswordForEmail(email, {  _10  redirectTo: 'https://example.com/update-password',  _10  })      `\
\
Response\
\
* * *\
\
Verify and log in through OTP\
-----------------------------\
\
Log in a user given a User supplied OTP or TokenHash received through mobile or email.\
\
*   The `verifyOtp` method takes in different verification types. If a phone number is used, the type can either be `sms` or `phone_change`. If an email address is used, the type can be one of the following: `email`, `recovery`, `invite` or `email_change` (`signup` and `magiclink` types are deprecated).\
*   The verification type used should be determined based on the corresponding auth method called before `verifyOtp` to sign up / sign-in a user.\
*   The `TokenHash` is contained in the [email templates](/docs/guides/auth/auth-email-templates)\
     and can be used to sign in. You may wish to use the hash with Magic Links for the PKCE flow for Server Side Auth. See [this guide](/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)\
     for more details.\
\
### Parameters\
\
*   paramsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Verify Signup One-Time Password (OTP)Verify Sms One-Time Password (OTP)Verify Email Auth (Token Hash)\
\
`     _10  const { data, error } = await supabase.auth.verifyOtp({ email, token, type: 'email'})      `\
\
Response\
\
* * *\
\
Retrieve a session\
------------------\
\
Returns the session, refreshing it if necessary.\
\
*   This method retrieves the current local session (i.e local storage).\
*   The session contains a signed JWT and unencoded session data.\
*   Since the unencoded session data is retrieved from the local storage medium, **do not** rely on it as a source of trusted data on the server. It could be tampered with by the sender. If you need verified, trustworthy user data, call [`getUser`](/docs/reference/javascript/auth-getuser)\
     instead.\
*   If the session has an expired access token, this method will use the refresh token to get a new session.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get the session data\
\
`     _10  const { data, error } = await supabase.auth.getSession()      `\
\
Response\
\
* * *\
\
Retrieve a new session\
----------------------\
\
Returns a new session, regardless of expiry status. Takes in an optional current session. If not passed in, then refreshSession() will attempt to retrieve it from getSession(). If the current session's refresh token is invalid, an error will be thrown.\
\
*   This method will refresh and return a new session whether the current one is expired or not.\
\
### Parameters\
\
*   currentSessionOptionalobject\
    \
    The current session. If passed in, it must contain a refresh token.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Refresh session using the current sessionRefresh session using a refresh token\
\
`     _10  const { data, error } = await supabase.auth.refreshSession()  _10  const { session, user } = data      `\
\
Response\
\
* * *\
\
Retrieve a user\
---------------\
\
Gets the current user details if there is an existing session. This method performs a network request to the Supabase Auth server, so the returned value is authentic and can be used to base authorization rules on.\
\
*   This method fetches the user object from the database instead of local session.\
*   This method is useful for checking if the user is authorized because it validates the user's access token JWT on the server.\
*   Should always be used when checking for user authorization on the server. On the client, you can instead use `getSession().session.user` for faster results. `getSession` is insecure on the server.\
\
### Parameters\
\
*   jwtOptionalstring\
    \
    Takes in an optional access token JWT. If no JWT is provided, the JWT from the current session is used.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get the logged in user with the current existing sessionGet the logged in user with a custom access token jwt\
\
`     _10  const { data: { user } } = await supabase.auth.getUser()      `\
\
Response\
\
* * *\
\
Update a user\
-------------\
\
Updates user data for a logged in user.\
\
*   In order to use the `updateUser()` method, the user needs to be signed in first.\
*   By default, email updates sends a confirmation link to both the user's current and new email. To only send a confirmation link to the user's new email, disable **Secure email change** in your project's [email auth provider settings](/dashboard/project/_/auth/providers)\
    .\
\
### Parameters\
\
*   attributesRequiredUserAttributes\
    \
    Details\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Update the email for an authenticated userUpdate the phone number for an authenticated userUpdate the password for an authenticated userUpdate the user's metadataUpdate the user's password with a nonce\
\
`     _10  const { data, error } = await supabase.auth.updateUser({  _10  email: 'new@email.com'  _10  })      `\
\
Response\
\
Notes\
\
* * *\
\
Retrieve identities linked to a user\
------------------------------------\
\
Gets all the identities linked to a user.\
\
*   The user needs to be signed in to call `getUserIdentities()`.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Returns a list of identities linked to the user\
\
`     _10  const { data, error } = await supabase.auth.getUserIdentities()      `\
\
Response\
\
* * *\
\
Link an identity to a user\
--------------------------\
\
Links an oauth identity to an existing user. This method supports the PKCE flow.\
\
*   The **Enable Manual Linking** option must be enabled from your [project's authentication settings](/dashboard/project/_/settings/auth)\
    .\
*   The user needs to be signed in to call `linkIdentity()`.\
*   If the candidate identity is already linked to the existing user or another user, `linkIdentity()` will fail.\
*   If `linkIdentity` is run in the browser, the user is automatically redirected to the returned URL. On the server, you should handle the redirect.\
\
### Parameters\
\
*   credentialsRequiredSignInWithOAuthCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Link an identity to a user\
\
`     _10  const { data, error } = await supabase.auth.linkIdentity({  _10  provider: 'github'  _10  })      `\
\
Response\
\
* * *\
\
Unlink an identity from a user\
------------------------------\
\
Unlinks an identity from a user by deleting it. The user will no longer be able to sign in with that identity once it's unlinked.\
\
*   The **Enable Manual Linking** option must be enabled from your [project's authentication settings](/dashboard/project/_/settings/auth)\
    .\
*   The user needs to be signed in to call `unlinkIdentity()`.\
*   The user must have at least 2 identities in order to unlink an identity.\
*   The identity to be unlinked must belong to the user.\
\
### Parameters\
\
*   identityRequiredUserIdentity\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Unlink an identity\
\
`     _10  // retrieve all identites linked to a user  _10  const identities = await supabase.auth.getUserIdentities()  _10  _10  // find the google identity  _10  const googleIdentity = identities.find(  _10  identity => identity.provider === 'google'  _10  )  _10  _10  // unlink the google identity  _10  const { error } = await supabase.auth.unlinkIdentity(googleIdentity)      `\
\
* * *\
\
Send a password reauthentication nonce\
--------------------------------------\
\
Sends a reauthentication OTP to the user's email or phone number. Requires the user to be signed-in.\
\
*   This method is used together with `updateUser()` when a user's password needs to be updated.\
*   If you require your user to reauthenticate before updating their password, you need to enable the **Secure password change** option in your [project's email provider settings](/dashboard/project/_/auth/providers)\
    .\
*   A user is only require to reauthenticate before updating their password if **Secure password change** is enabled and the user **hasn't recently signed in**. A user is deemed recently signed in if the session was created in the last 24 hours.\
*   This method will send a nonce to the user's email. If the user doesn't have a confirmed email address, the method will send the nonce to the user's confirmed phone number instead.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Send reauthentication nonce\
\
`     _10  const { error } = await supabase.auth.reauthenticate()      `\
\
Notes\
\
* * *\
\
Resend an OTP\
-------------\
\
Resends an existing signup confirmation email, email change email, SMS OTP or phone change OTP.\
\
*   Resends a signup confirmation, email change or phone change email to the user.\
*   Passwordless sign-ins can be resent by calling the `signInWithOtp()` method again.\
*   Password recovery emails can be resent by calling the `resetPasswordForEmail()` method again.\
*   This method will only resend an email or phone OTP to the user if there was an initial signup, email change or phone change request being made.\
*   You can specify a redirect url when you resend an email link using the `emailRedirectTo` option.\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Resend an email signup confirmationResend a phone signup confirmationResend email change emailResend phone change OTP\
\
`     _10  const { error } = await supabase.auth.resend({  _10  type: 'signup',  _10  email: 'email@example.com',  _10  options: {  _10  emailRedirectTo: 'https://example.com/welcome'  _10  }  _10  })      `\
\
Notes\
\
* * *\
\
Set the session data\
--------------------\
\
Sets the session data from the current session. If the current session is expired, setSession will take care of refreshing it to obtain a new session. If the refresh token or access token in the current session is invalid, an error will be thrown.\
\
*   This method sets the session using an `access_token` and `refresh_token`.\
*   If successful, a `SIGNED_IN` event is emitted.\
\
### Parameters\
\
*   currentSessionRequiredobject\
    \
    The current session that minimally contains an access token and refresh token.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Set the session\
\
`     _10  const { data, error } = await supabase.auth.setSession({  _10  access_token,  _10  refresh_token  _10  })      `\
\
Response\
\
Notes\
\
* * *\
\
Exchange an auth code for a session\
-----------------------------------\
\
Log in an existing user by exchanging an Auth Code issued during the PKCE flow.\
\
*   Used when `flowType` is set to `pkce` in client options.\
\
### Parameters\
\
*   authCodeRequiredstring\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Exchange Auth Code\
\
`     _10  supabase.auth.exchangeCodeForSession('34e770dd-9ff9-416c-87fa-43b31d7ef225')      `\
\
Response\
\
* * *\
\
Start auto-refresh session (non-browser)\
----------------------------------------\
\
Starts an auto-refresh process in the background. The session is checked every few seconds. Close to the time of expiration a process is started to refresh the session. If refreshing fails it will be retried for as long as necessary.\
\
*   Only useful in non-browser environments such as React Native or Electron.\
*   The Supabase Auth library automatically starts and stops proactively refreshing the session when a tab is focused or not.\
*   On non-browser platforms, such as mobile or desktop apps built with web technologies, the library is not able to effectively determine whether the application is _focused_ or not.\
*   To give this hint to the application, you should be calling this method when the app is in focus and calling `supabase.auth.stopAutoRefresh()` when it's out of focus.\
\
### Return Type\
\
Promise<void>\
\
Start and stop auto refresh in React Native\
\
`     _10  import { AppState } from 'react-native'  _10  _10  // make sure you register this only once!  _10  AppState.addEventListener('change', (state) => {  _10  if (state === 'active') {  _10  supabase.auth.startAutoRefresh()  _10  } else {  _10  supabase.auth.stopAutoRefresh()  _10  }  _10  })      `\
\
* * *\
\
Stop auto-refresh session (non-browser)\
---------------------------------------\
\
Stops an active auto refresh process running in the background (if any).\
\
*   Only useful in non-browser environments such as React Native or Electron.\
*   The Supabase Auth library automatically starts and stops proactively refreshing the session when a tab is focused or not.\
*   On non-browser platforms, such as mobile or desktop apps built with web technologies, the library is not able to effectively determine whether the application is _focused_ or not.\
*   When your application goes in the background or out of focus, call this method to stop the proactive refreshing of the session.\
\
### Return Type\
\
Promise<void>\
\
Start and stop auto refresh in React Native\
\
`     _10  import { AppState } from 'react-native'  _10  _10  // make sure you register this only once!  _10  AppState.addEventListener('change', (state) => {  _10  if (state === 'active') {  _10  supabase.auth.startAutoRefresh()  _10  } else {  _10  supabase.auth.stopAutoRefresh()  _10  }  _10  })      `\
\
* * *\
\
Auth MFA\
--------\
\
This section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.\
\
Currently, there is support for time-based one-time password (TOTP) and phone verification code as the 2nd factor. Recovery codes are not supported but users can enroll multiple factors, with an upper limit of 10.\
\
Having a 2nd factor for recovery frees the user of the burden of having to store their recovery codes somewhere. It also reduces the attack surface since multiple recovery codes are usually generated compared to just having 1 backup factor.\
\
* * *\
\
Enroll a factor\
---------------\
\
Starts the enrollment process for a new Multi-Factor Authentication (MFA) factor. This method creates a new `unverified` factor. To verify a factor, present the QR code or secret to the user and ask them to add it to their authenticator app. The user has to enter the code from their authenticator app to verify it.\
\
*   Use `totp` or `phone` as the `factorType` and use the returned `id` to create a challenge.\
*   To create a challenge, see [`mfa.challenge()`](/docs/reference/javascript/auth-mfa-challenge)\
    .\
*   To verify a challenge, see [`mfa.verify()`](/docs/reference/javascript/auth-mfa-verify)\
    .\
*   To create and verify a TOTP challenge in a single step, see [`mfa.challengeAndVerify()`](/docs/reference/javascript/auth-mfa-challengeandverify)\
    .\
*   To generate a QR code for the `totp` secret in Next.js, you can do the following:\
\
`     _10  <Image src=\{data.totp.qr_code\} alt=\{data.totp.uri\} layout="fill"></Image>      `\
\
*   The `challenge` and `verify` steps are separated when using Phone factors as the user will need time to receive and input the code obtained from the SMS in challenge.\
\
### Parameters\
\
*   paramsRequiredMFAEnrollParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Enroll a time-based, one-time password (TOTP) factorEnroll a Phone Factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.enroll({  _10  factorType: 'totp',  _10  friendlyName: 'your_friendly_name'  _10  })  _10  _10  // Use the id to create a challenge.  _10  // The challenge can be verified by entering the code generated from the authenticator app.  _10  // The code will be generated upon scanning the qr_code or entering the secret into the authenticator app.  _10  const { id, type, totp: { qr_code, secret, uri }, friendly_name } = data  _10  const challenge = await supabase.auth.mfa.challenge({ factorId: id });      `\
\
Response\
\
* * *\
\
Create a challenge\
------------------\
\
Prepares a challenge used to verify that a user has access to a MFA factor.\
\
*   An [enrolled factor](/docs/reference/javascript/auth-mfa-enroll)\
     is required before creating a challenge.\
*   To verify a challenge, see [`mfa.verify()`](/docs/reference/javascript/auth-mfa-verify)\
    .\
*   A phone factor sends a code to the user upon challenge. The channel defaults to `sms` unless otherwise specified.\
\
### Parameters\
\
*   paramsRequiredMFAChallengeParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create a challenge for a factorCreate a challenge for a phone factorCreate a challenge for a phone factor (WhatsApp)\
\
`     _10  const { data, error } = await supabase.auth.mfa.challenge({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225'  _10  })      `\
\
Response\
\
* * *\
\
Verify a challenge\
------------------\
\
Verifies a code against a challenge. The verification code is provided by the user by entering a code seen in their authenticator app.\
\
*   To verify a challenge, please [create a challenge](/docs/reference/javascript/auth-mfa-challenge)\
     first.\
\
### Parameters\
\
*   paramsRequiredMFAVerifyParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Verify a challenge for a factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.verify({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  challengeId: '4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15',  _10  code: '123456'  _10  })      `\
\
Response\
\
* * *\
\
Create and verify a challenge\
-----------------------------\
\
Helper method which creates a challenge and immediately uses the given code to verify against it thereafter. The verification code is provided by the user by entering a code seen in their authenticator app.\
\
*   Intended for use with only TOTP factors.\
*   An [enrolled factor](/docs/reference/javascript/auth-mfa-enroll)\
     is required before invoking `challengeAndVerify()`.\
*   Executes [`mfa.challenge()`](/docs/reference/javascript/auth-mfa-challenge)\
     and [`mfa.verify()`](/docs/reference/javascript/auth-mfa-verify)\
     in a single step.\
\
### Parameters\
\
*   paramsRequiredMFAChallengeAndVerifyParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create and verify a challenge for a factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.challengeAndVerify({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  code: '123456'  _10  })      `\
\
Response\
\
* * *\
\
Unenroll a factor\
-----------------\
\
Unenroll removes a MFA factor. A user has to have an `aal2` authenticator level in order to unenroll a `verified` factor.\
\
### Parameters\
\
*   paramsRequiredMFAUnenrollParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Unenroll a factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.unenroll({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  })      `\
\
Response\
\
* * *\
\
Get Authenticator Assurance Level\
---------------------------------\
\
Returns the Authenticator Assurance Level (AAL) for the active session.\
\
*   Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.\
*   In Supabase, having an AAL of `aal1` refers to having the 1st factor of authentication such as an email and password or OAuth sign-in while `aal2` refers to the 2nd factor of authentication such as a time-based, one-time-password (TOTP) or Phone factor.\
*   If the user has a verified factor, the `nextLevel` field will return `aal2`, else, it will return `aal1`.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get the AAL details of a session\
\
`     _10  const { data, error } = await supabase.auth.mfa.getAuthenticatorAssuranceLevel()  _10  const { currentLevel, nextLevel, currentAuthenticationMethods } = data      `\
\
Response\
\
* * *\
\
Auth Admin\
----------\
\
*   Any method under the `supabase.auth.admin` namespace requires a `service_role` key.\
*   These methods are considered admin methods and should be called on a trusted server. Never expose your `service_role` key in the browser.\
\
Create server-side auth client\
\
`     _11  import { createClient } from '@supabase/supabase-js'  _11  _11  const supabase = createClient(supabase_url, service_role_key, {  _11  auth: {  _11  autoRefreshToken: false,  _11  persistSession: false  _11  }  _11  })  _11  _11  // Access auth admin api  _11  const adminAuthClient = supabase.auth.admin      `\
\
* * *\
\
Retrieve a user\
---------------\
\
Get user by id.\
\
*   Fetches the user object from the database based on the user's id.\
*   The `getUserById()` method requires the user's id which maps to the `auth.users.id` column.\
\
### Parameters\
\
*   uidRequiredstring\
    \
    The user's unique identifier\
    \
    This function should only be called on a server. Never expose your `service_role` key in the browser.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Fetch the user object using the access\_token jwt\
\
`     _10  const { data, error } = await supabase.auth.admin.getUserById(1)      `\
\
Response\
\
* * *\
\
List all users\
--------------\
\
Get a list of users.\
\
*   Defaults to return 50 users per page.\
\
### Parameters\
\
*   paramsOptionalPageParams\
    \
    An object which supports `page` and `perPage` as numbers, to alter the paginated results.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get a page of usersPaginated list of users\
\
`     _10  const { data: { users }, error } = await supabase.auth.admin.listUsers()      `\
\
* * *\
\
Create a user\
-------------\
\
Creates a new user. This function should only be called on a server. Never expose your `service_role` key in the browser.\
\
*   To confirm the user's email address or phone number, set `email_confirm` or `phone_confirm` to true. Both arguments default to false.\
*   `createUser()` will not send a confirmation email to the user. You can use [`inviteUserByEmail()`](/docs/reference/javascript/auth-admin-inviteuserbyemail)\
     if you want to send them an email invite instead.\
*   If you are sure that the created user's email or phone number is legitimate and verified, you can set the `email_confirm` or `phone_confirm` param to `true`.\
\
### Parameters\
\
*   attributesRequiredAdminUserAttributes\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
With custom user metadataAuto-confirm the user's emailAuto-confirm the user's phone number\
\
`     _10  const { data, error } = await supabase.auth.admin.createUser({  _10  email: 'user@email.com',  _10  password: 'password',  _10  user_metadata: { name: 'Yoda' }  _10  })      `\
\
Response\
\
* * *\
\
Delete a user\
-------------\
\
Delete a user. Requires a `service_role` key.\
\
*   The `deleteUser()` method requires the user's ID, which maps to the `auth.users.id` column.\
\
### Parameters\
\
*   idRequiredstring\
    \
    The user id you want to remove.\
    \
*   shouldSoftDeleteRequiredboolean\
    \
    If true, then the user will be soft-deleted (setting `deleted_at` to the current timestamp and disabling their account while preserving their data) from the auth schema. Defaults to false for backward compatibility.\
    \
    This function should only be called on a server. Never expose your `service_role` key in the browser.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Removes a user\
\
`     _10  const { data, error } = await supabase.auth.admin.deleteUser(  _10  '715ed5db-f090-4b8c-a067-640ecee36aa0'  _10  )      `\
\
Response\
\
* * *\
\
Send an email invite link\
-------------------------\
\
Sends an invite link to an email address.\
\
*   Sends an invite link to the user's email address.\
*   The `inviteUserByEmail()` method is typically used by administrators to invite users to join the application.\
*   Note that PKCE is not supported when using `inviteUserByEmail`. This is because the browser initiating the invite is often different from the browser accepting the invite which makes it difficult to provide the security guarantees required of the PKCE flow.\
\
### Parameters\
\
*   emailRequiredstring\
    \
    The email address of the user.\
    \
*   optionsRequiredobject\
    \
    Additional options to be included when inviting.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Invite a user\
\
`     _10  const { data, error } = await supabase.auth.admin.inviteUserByEmail('email@example.com')      `\
\
Response\
\
* * *\
\
Generate an email link\
----------------------\
\
Generates email links and OTPs to be sent via a custom email provider.\
\
*   The following types can be passed into `generateLink()`: `signup`, `magiclink`, `invite`, `recovery`, `email_change_current`, `email_change_new`, `phone_change`.\
*   `generateLink()` only generates the email link for `email_change_email` if the **Secure email change** is enabled in your project's [email auth provider settings](/dashboard/project/_/auth/providers)\
    .\
*   `generateLink()` handles the creation of the user for `signup`, `invite` and `magiclink`.\
\
### Parameters\
\
*   paramsRequiredGenerateLinkParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Generate a signup linkGenerate an invite linkGenerate a magic linkGenerate a recovery linkGenerate links to change current email address\
\
`     _10  const { data, error } = await supabase.auth.admin.generateLink({  _10  type: 'signup',  _10  email: 'email@example.com',  _10  password: 'secret'  _10  })      `\
\
Response\
\
* * *\
\
Update a user\
-------------\
\
Updates the user data.\
\
### Parameters\
\
*   uidRequiredstring\
    \
*   attributesRequiredAdminUserAttributes\
    \
    The data you want to update.\
    \
    This function should only be called on a server. Never expose your `service_role` key in the browser.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Updates a user's emailUpdates a user's passwordUpdates a user's metadataUpdates a user's app\_metadataConfirms a user's email addressConfirms a user's phone number\
\
`     _10  const { data: user, error } = await supabase.auth.admin.updateUserById(  _10  '11111111-1111-1111-1111-111111111111',  _10  { email: 'new@email.com' }  _10  )      `\
\
Response\
\
* * *\
\
Delete a factor for a user\
--------------------------\
\
Deletes a factor on a user. This will log the user out of all active sessions if the deleted factor was verified.\
\
### Parameters\
\
*   paramsRequiredAuthMFAAdminDeleteFactorParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Delete a factor for a user\
\
`     _10  const { data, error } = await supabase.auth.admin.mfa.deleteFactor({  _10  id: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  userId: 'a89baba7-b1b7-440f-b4bb-91026967f66b',  _10  })      `\
\
Response\
\
* * *\
\
Invokes a Supabase Edge Function.\
---------------------------------\
\
Invokes a function\
\
Invoke a Supabase Edge Function.\
\
*   Requires an Authorization header.\
*   Invoke params generally match the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)\
     spec.\
*   When you pass in a body to your function, we automatically attach the Content-Type header for `Blob`, `ArrayBuffer`, `File`, `FormData` and `String`. If it doesn't match any of these types we assume the payload is `json`, serialize it and attach the `Content-Type` header as `application/json`. You can override this behavior by passing in a `Content-Type` header of your own.\
*   Responses are automatically parsed as `json`, `blob` and `form-data` depending on the `Content-Type` header sent by your function. Responses are parsed as `text` by default.\
\
### Parameters\
\
*   functionNameRequiredstring\
    \
    The name of the Function to invoke.\
    \
*   optionsRequiredFunctionInvokeOptions\
    \
    Options for invoking the Function.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Basic invocationError handlingPassing custom headersCalling with DELETE HTTP verbInvoking a Function in the UsEast1 regionCalling with GET HTTP verb\
\
`     _10  const { data, error } = await supabase.functions.invoke('hello', {  _10  body: { foo: 'bar' }  _10  })      `\
\
* * *\
\
Subscribe to channel\
--------------------\
\
Creates an event handler that listens to changes.\
\
*   By default, Broadcast and Presence are enabled for all projects.\
*   By default, listening to database changes is disabled for new projects due to database performance and security concerns. You can turn it on by managing Realtime's [replication](/docs/guides/api#realtime-api-overview)\
    .\
*   You can receive the "previous" data for updates and deletes by setting the table's `REPLICA IDENTITY` to `FULL` (e.g., `ALTER TABLE your_table REPLICA IDENTITY FULL;`).\
*   Row level security is not applied to delete statements. When RLS is enabled and replica identity is set to full, only the primary key is sent to clients.\
\
### Parameters\
\
*   typeRequiredUnion: expand to see options\
    \
    Details\
    \
*   filterRequiredUnion: expand to see options\
    \
    Details\
    \
*   callbackRequiredfunction\
    \
    Details\
    \
\
Listen to broadcast messagesListen to presence syncListen to presence joinListen to presence leaveListen to all database changesListen to a specific tableListen to insertsListen to updatesListen to deletesListen to multiple eventsListen to row level changes\
\
`     _13  const channel = supabase.channel("room1")  _13  _13  channel.on("broadcast", { event: "cursor-pos" }, (payload) => {  _13  console.log("Cursor position received!", payload);  _13  }).subscribe((status) => {  _13  if (status === "SUBSCRIBED") {  _13  channel.send({  _13  type: "broadcast",  _13  event: "cursor-pos",  _13  payload: { x: Math.random(), y: Math.random() },  _13  });  _13  }  _13  });      `\
\
* * *\
\
Unsubscribe from a channel\
--------------------------\
\
Unsubscribes and removes Realtime channel from Realtime client.\
\
*   Removing a channel is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.\
\
### Parameters\
\
*   channelRequired@supabase/realtime-js.RealtimeChannel\
    \
    The name of the Realtime channel.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Removes a channel\
\
`     _10  supabase.removeChannel(myChannel)      `\
\
* * *\
\
Unsubscribe from all channels\
-----------------------------\
\
Unsubscribes and removes all Realtime channels from Realtime client.\
\
*   Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.\
\
### Return Type\
\
Promise<Array<Union: expand to see options>>\
\
Details\
\
Remove all channels\
\
`     _10  supabase.removeAllChannels()      `\
\
* * *\
\
Retrieve all channels\
---------------------\
\
Returns all Realtime channels.\
\
### Return Type\
\
Array<@supabase/realtime-js.RealtimeChannel>\
\
Get all channels\
\
`     _10  const channels = supabase.getChannels()      `\
\
* * *\
\
Broadcast a message\
-------------------\
\
Sends a message into the channel.\
\
Broadcast a message to all connected clients to a channel.\
\
*   When using REST you don't need to subscribe to the channel\
*   REST calls are only available from 2.37.0 onwards\
\
### Parameters\
\
*   argsRequiredobject\
    \
    Arguments to send to channel\
    \
    Details\
    \
*   optsRequired{ \[key: string\]: any }\
    \
    Options to be used during the send process\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Send a message via websocketSend a message via REST\
\
`     _11  supabase  _11  .channel('room1')  _11  .subscribe((status) => {  _11  if (status === 'SUBSCRIBED') {  _11  channel.send({  _11  type: 'broadcast',  _11  event: 'cursor-pos',  _11  payload: { x: Math.random(), y: Math.random() },  _11  })  _11  }  _11  })      `\
\
Response\
\
* * *\
\
Create a bucket\
---------------\
\
Creates a new Storage bucket\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `insert`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    A unique identifier for the bucket you are creating.\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .createBucket('avatars', {  _10  public: false,  _10  allowedMimeTypes: ['image/png'],  _10  fileSizeLimit: 1024  _10  })      `\
\
Response\
\
* * *\
\
Retrieve a bucket\
-----------------\
\
Retrieves the details of an existing Storage bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    The unique identifier of the bucket you would like to retrieve.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .getBucket('avatars')      `\
\
Response\
\
* * *\
\
List all buckets\
----------------\
\
Retrieves the details of all Storage buckets within an existing project.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
List buckets\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .listBuckets()      `\
\
Response\
\
* * *\
\
Update a bucket\
---------------\
\
Updates a Storage bucket\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select` and `update`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    A unique identifier for the bucket you are updating.\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Update bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .updateBucket('avatars', {  _10  public: false,  _10  allowedMimeTypes: ['image/png'],  _10  fileSizeLimit: 1024  _10  })      `\
\
Response\
\
* * *\
\
Delete a bucket\
---------------\
\
Deletes an existing bucket. A bucket can't be deleted with existing objects inside it. You must first `empty()` the bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select` and `delete`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    The unique identifier of the bucket you would like to delete.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Delete bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .deleteBucket('avatars')      `\
\
Response\
\
* * *\
\
Empty a bucket\
--------------\
\
Removes all objects inside a single bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select`\
    *   `objects` table permissions: `select` and `delete`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    The unique identifier of the bucket you would like to empty.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Empty bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .emptyBucket('avatars')      `\
\
Response\
\
* * *\
\
Upload a file\
-------------\
\
Uploads a file to an existing bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: only `insert` when you are uploading new files and `select`, `insert` and `update` when you are upserting files\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
*   For React Native, using either `Blob`, `File` or `FormData` does not work as intended. Upload file using `ArrayBuffer` from base64 file data instead, see example below.\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.\
    \
*   fileBodyRequiredFileBody\
    \
    The body of the file to be stored in the bucket.\
    \
*   fileOptionsOptionalFileOptions\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Upload fileUpload file using \`ArrayBuffer\` from base64 file data\
\
`     _10  const avatarFile = event.target.files[0]  _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .upload('public/avatar1.png', avatarFile, {  _10  cacheControl: '3600',  _10  upsert: false  _10  })      `\
\
Response\
\
* * *\
\
Download a file\
---------------\
\
Downloads a file from a private bucket. For public buckets, make a request to the URL returned from `getPublicUrl` instead.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The full path and file name of the file to be downloaded. For example `folder/image.png`.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Download fileDownload file with transformations\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .download('folder/avatar1.png')      `\
\
Response\
\
* * *\
\
List all files in a bucket\
--------------------------\
\
Lists all the files within a bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathOptionalstring\
    \
    The folder path.\
    \
*   optionsOptionalSearchOptions\
    \
    Details\
    \
*   parametersOptionalFetchParameters\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
List files in a bucketSearch files in a bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .list('folder', {  _10  limit: 100,  _10  offset: 0,  _10  sortBy: { column: 'name', order: 'asc' },  _10  })      `\
\
Response\
\
* * *\
\
Replace an existing file\
------------------------\
\
Replaces an existing file at the specified path with a new one.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `update` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
*   For React Native, using either `Blob`, `File` or `FormData` does not work as intended. Update file using `ArrayBuffer` from base64 file data instead, see example below.\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The relative file path. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to update.\
    \
*   fileBodyRequiredUnion: expand to see options\
    \
    The body of the file to be stored in the bucket.\
    \
    Details\
    \
*   fileOptionsOptionalFileOptions\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Update fileUpdate file using \`ArrayBuffer\` from base64 file data\
\
`     _10  const avatarFile = event.target.files[0]  _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .update('public/avatar1.png', avatarFile, {  _10  cacheControl: '3600',  _10  upsert: true  _10  })      `\
\
Response\
\
* * *\
\
Move an existing file\
---------------------\
\
Moves an existing file to a new path in the same bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `update` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   fromPathRequiredstring\
    \
    The original file path, including the current file name. For example `folder/image.png`.\
    \
*   toPathRequiredstring\
    \
    The new file path, including the new file name. For example `folder/image-new.png`.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Move file\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .move('public/avatar1.png', 'private/avatar2.png')      `\
\
Response\
\
* * *\
\
Copy an existing file\
---------------------\
\
Copies an existing file to a new path in the same bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `insert` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   fromPathRequiredstring\
    \
    The original file path, including the current file name. For example `folder/image.png`.\
    \
*   toPathRequiredstring\
    \
    The new file path, including the new file name. For example `folder/image-copy.png`.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Copy file\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .copy('public/avatar1.png', 'private/avatar2.png')      `\
\
Response\
\
* * *\
\
Delete files in a bucket\
------------------------\
\
Deletes files within the same bucket\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `delete` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathsRequiredArray<string>\
    \
    An array of files to delete, including the path and file name. For example \[`'folder/image.png'`\].\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Delete file\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .remove(['folder/avatar1.png'])      `\
\
Response\
\
* * *\
\
Create a signed URL\
-------------------\
\
Creates a signed URL. Use a signed URL to share a file for a fixed amount of time.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the current file name. For example `folder/image.png`.\
    \
*   expiresInRequirednumber\
    \
    The number of seconds until the signed URL expires. For example, `60` for a URL which is valid for one minute.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create Signed URLCreate a signed URL for an asset with transformationsCreate a signed URL which triggers the download of the asset\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .createSignedUrl('folder/avatar1.png', 60)      `\
\
Response\
\
* * *\
\
Create signed URLs\
------------------\
\
Creates multiple signed URLs. Use a signed URL to share a file for a fixed amount of time.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathsRequiredArray<string>\
    \
    The file paths to be downloaded, including the current file names. For example `['folder/image.png', 'folder2/image2.png']`.\
    \
*   expiresInRequirednumber\
    \
    The number of seconds until the signed URLs expire. For example, `60` for URLs which are valid for one minute.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create Signed URLs\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .createSignedUrls(['folder/avatar1.png', 'folder/avatar2.png'], 60)      `\
\
Response\
\
* * *\
\
Create signed upload URL\
------------------------\
\
Creates a signed upload URL. Signed upload URLs can be used to upload files to the bucket without further authentication. They are valid for 2 hours.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `insert`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the current file name. For example `folder/image.png`.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create Signed Upload URL\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .createSignedUploadUrl('folder/cat.jpg')      `\
\
Response\
\
* * *\
\
Upload to a signed URL\
----------------------\
\
Upload a file with a token generated from `createSignedUploadUrl`.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.\
    \
*   tokenRequiredstring\
    \
    The token generated from `createSignedUploadUrl`\
    \
*   fileBodyRequiredFileBody\
    \
    The body of the file to be stored in the bucket.\
    \
*   fileOptionsOptionalFileOptions\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Upload to a signed URL\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .uploadToSignedUrl('folder/cat.jpg', 'token-from-createSignedUploadUrl', file)      `\
\
Response\
\
* * *\
\
Retrieve public URL\
-------------------\
\
A simple convenience function to get the URL for an asset in a public bucket. If you do not want to use this function, you can construct the public URL by concatenating the bucket URL with the path to the asset. This function does not verify if the bucket is public. If a public URL is created for a bucket which is not public, you will not be able to download the asset.\
\
*   The bucket needs to be set to public, either via [updateBucket()](/docs/reference/javascript/storage-updatebucket)\
     or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard)\
    , clicking the overflow menu on a bucket and choosing "Make public"\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The path and name of the file to generate the public URL for. For example `folder/image.png`.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
object\
\
Details\
\
Returns the URL for an asset in a public bucketReturns the URL for an asset in a public bucket with transformationsReturns the URL which triggers the download of an asset in a public bucket\
\
`     _10  const { data } = supabase  _10  .storage  _10  .from('public-bucket')  _10  .getPublicUrl('folder/avatar1.png')      `\
\
Response\
\
* * *\
\
Release Notes\
-------------\
\
Supabase.js v2 release notes.\
\
Install the latest version of @supabase/supabase-js\
\
Terminal\
\
`     _10  npm install @supabase/supabase-js      `\
\
### Explicit constructor options[#](#explicit-constructor-options)\
\
All client specific options within the constructor are keyed to the library.\
\
See [PR](https://github.com/supabase/supabase-js/pull/458)\
:\
\
`     _19  const supabase = createClient(apiURL, apiKey, {  _19  db: {  _19  schema: 'public',  _19  },  _19  auth: {  _19  storage: AsyncStorage,  _19  autoRefreshToken: true,  _19  persistSession: true,  _19  detectSessionInUrl: true,  _19  },  _19  realtime: {  _19  channels,  _19  endpoint,  _19  },  _19  global: {  _19  fetch: customFetch,  _19  headers: DEFAULT_HEADERS,  _19  },  _19  })      `\
\
### TypeScript support[#](#typescript-support)\
\
The libraries now support typescript.\
\
v1.0\
\
``     _10  // previously definitions were injected in the `from()` method  _10  supabase.from<Definitions['Message']>('messages').select('\*')      ``\
\
* * *\
\
v2.0\
\
``     _10  import type { Database } from './DatabaseDefinitions'  _10  _10  // definitions are injected in `createClient()`  _10  const supabase = createClient<Database>(SUPABASE_URL, ANON_KEY)  _10  _10  const { data } = await supabase.from('messages').select().match({ id: 1 })      ``\
\
Types can be generated via the CLI:\
\
Terminal\
\
`     _10  supabase start  _10  supabase gen types typescript --local > DatabaseDefinitions.ts      `\
\
### Data operations return minimal[#](#data-operations-return-minimal)\
\
`.insert()` / `.upsert()` / `.update()` / `.delete()` don't return rows by default: [PR](https://github.com/supabase/postgrest-js/pull/276)\
.\
\
Previously, these methods return inserted/updated/deleted rows by default (which caused [some confusion](https://github.com/supabase/supabase/discussions/1548)\
), and you can opt to not return it by specifying `returning: 'minimal'`. Now the default behavior is to not return rows. To return inserted/updated/deleted rows, add a `.select()` call at the end, e.g.:\
\
`     _10  const { data, error } = await supabase  _10  .from('my_table')  _10  .delete()  _10  .eq('id', 1)  _10  .select()      `\
\
### New ordering defaults[#](#new-ordering-defaults)\
\
`.order()` now defaults to Postgres’s default: [PR](https://github.com/supabase/postgrest-js/pull/283)\
.\
\
Previously `nullsFirst` defaults to `false` , meaning `null`s are ordered last. This is bad for performance if e.g. the column uses an index with `NULLS FIRST` (which is the default direction for indexes).\
\
### Cookies and localstorage namespace[#](#cookies-and-localstorage-namespace)\
\
Storage key name in the Auth library has changed to include project reference which means that existing websites that had their JWT expiry set to a longer time could find their users logged out with this upgrade.\
\
``     _10  const defaultStorageKey = `sb-${new URL(this.authUrl).hostname.split('.')[0]}-auth-token`      ``\
\
### New Auth Types[#](#new-auth-types)\
\
Typescript typings have been reworked. `Session` interface now guarantees that it will always have an `access_token`, `refresh_token` and `user`\
\
./types.ts\
\
`     _10  interface Session {  _10  provider_token?: string | null  _10  access_token: string  _10  expires_in?: number  _10  expires_at?: number  _10  refresh_token: string  _10  token_type: string  _10  user: User  _10  }      `\
\
### New Auth methods[#](#new-auth-methods)\
\
We're removing the `signIn()` method in favor of more explicit function signatures: `signInWithPassword()`, `signInWithOtp()`, and `signInWithOAuth()`.\
\
v1.0\
\
`     _10  const { data } = await supabase.auth.signIn({  _10  email: 'hello@example',  _10  password: 'pass',  _10  })      `\
\
* * *\
\
v2.0\
\
`     _10  const { data } = await supabase.auth.signInWithPassword({  _10  email: 'hello@example',  _10  password: 'pass',  _10  })      `\
\
### New Realtime methods[#](#new-realtime-methods)\
\
There is a new `channel()` method in the Realtime library, which will be used for our Multiplayer updates.\
\
We will deprecate the `.from().on().subscribe()` method previously used for listening to postgres changes.\
\
`     _21  supabase  _21  .channel('any_string_you_want')  _21  .on('presence', { event: 'track' }, (payload) => {  _21  console.log(payload)  _21  })  _21  .subscribe()  _21  _21  supabase  _21  .channel('any_string_you_want')  _21  .on(  _21  'postgres_changes',  _21  {  _21  event: 'INSERT',  _21  schema: 'public',  _21  table: 'movies',  _21  },  _21  (payload) => {  _21  console.log(payload)  _21  }  _21  )  _21  .subscribe()      `\
\
### Deprecated setAuth()[#](#deprecated-setauth)\
\
Deprecated and removed `setAuth()` . To set a custom `access_token` jwt instead, pass the custom header into the `createClient()` method provided: ([PR](https://github.com/supabase/gotrue-js/pull/340)\
)\
\
### All changes[#](#all-changes)\
\
*   `supabase-js`\
    *   `shouldThrowOnError` has been removed until all the client libraries support this option ([PR](https://github.com/supabase/supabase-js/pull/490)\
        ).\
*   `postgrest-js`\
    *   TypeScript typings have been reworked [PR](https://github.com/supabase/postgrest-js/pull/279)\
        \
    *   Use `undefined` instead of `null` for function params, types, etc. ([https://github.com/supabase/postgrest-js/pull/278](https://github.com/supabase/postgrest-js/pull/278)\
        )\
    *   Some features are now obsolete: ([https://github.com/supabase/postgrest-js/pull/275](https://github.com/supabase/postgrest-js/pull/275)\
        )\
        *   filter shorthands (e.g. `cs` vs. `contains`)\
        *   `body` in response (vs. `data`)\
        *   `upsert`ing through the `.insert()` method\
        *   `auth` method on `PostgrestClient`\
        *   client-level `throwOnError`\
*   `gotrue-js`\
    *   `supabase-js` client allows passing a `storageKey` param which will allow the user to set the key used in local storage for storing the session. By default, this will be namespace-d with the supabase project ref. ([PR](https://github.com/supabase/supabase-js/pull/460)\
        )\
    *   `signIn` method is now split into `signInWithPassword` , `signInWithOtp` , `signInWithOAuth` ([PR](https://github.com/supabase/gotrue-js/pull/304)\
        )\
    *   Deprecated and removed `session()` , `user()` in favour of using `getSession()` instead. `getSession()` will always return a valid session if a user is already logged in, meaning no more random logouts. ([PR](https://github.com/supabase/gotrue-js/pull/299)\
        )\
    *   Deprecated and removed setting for `multitab` support because `getSession()` and gotrue’s reuse interval setting takes care of session management across multiple tabs ([PR](https://github.com/supabase/gotrue-js/pull/366)\
        )\
    *   No more throwing of random errors, gotrue-js v2 always returns a custom error type: ([PR](https://github.com/supabase/gotrue-js/pull/341)\
        )\
        *   `AuthSessionMissingError`\
            *   Indicates that a session is expected but missing\
        *   `AuthNoCookieError`\
            *   Indicates that a cookie is expected but missing\
        *   `AuthInvalidCredentialsError`\
            *   Indicates that the incorrect credentials were passed\
    *   Renamed the `api` namespace to `admin` , the `admin` namespace will only contain methods that should only be used in a trusted server-side environment with the service role key\
    *   Moved `resetPasswordForEmail` , `getUser` and `updateUser` to the `GoTrueClient` which means they will be accessible from the `supabase.auth` namespace in `supabase-js` instead of having to do `supabase.auth.api` to access them\
    *   Removed `sendMobileOTP` , `sendMagicLinkEmail` in favor of `signInWithOtp`\
    *   Removed `signInWithEmail`, `signInWithPhone` in favor of `signInWithPassword`\
    *   Removed `signUpWithEmail` , `signUpWithPhone` in favor of `signUp`\
    *   Replaced `update` with `updateUser`\
*   `storage-js`\
    *   Return types are more strict. Functions types used to indicate that the data returned could be null even if there was no error. We now make use of union types which only mark the data as null if there is an error and vice versa. ([PR](https://github.com/supabase/storage-js/pull/60)\
        )\
    *   The `upload` and `update` function returns the path of the object uploaded as the `path` parameter. Previously the returned value had the bucket name prepended to the path which made it harder to pass the value on to other storage-js methods since all methods take the bucket name and path separately. We also chose to call the returned value `path` instead of `Key` ([PR](https://github.com/supabase/storage-js/pull/75)\
        )\
    *   `getPublicURL` only returns the public URL inside the data object. This keeps it consistent with our other methods of returning only within the data object. No error is returned since this method cannot does not throw an error ([PR](https://github.com/supabase/storage-js/pull/93)\
        )\
    *   signed urls are returned as `signedUrl` instead of `signedURL` in both `createSignedUrl` and `createSignedUrls` ([PR](https://github.com/supabase/storage-js/pull/94)\
        )\
    *   Encodes URLs returned by `createSignedUrl`, `createSignedUrls` and `getPublicUrl` ([PR](https://github.com/supabase/storage-js/pull/86)\
        )\
    *   `createsignedUrl` used to return a url directly and and within the data object. This was inconsistent. Now we always return values only inside the data object across all methods. ([PR](https://github.com/supabase/storage-js/pull/88)\
        )\
    *   `createBucket` returns a data object instead of the name of the bucket directly. ([PR](https://github.com/supabase/storage-js/pull/89)\
        )\
    *   Fixed types for metadata ([PR](https://github.com/supabase/storage-js/pull/90)\
        )\
    *   Better error types make it easier to track down what went wrong quicker.\
    *   `SupabaseStorageClient` is no longer exported. Use `StorageClient` instead. ([PR](https://github.com/supabase/storage-js/pull/92)\
        ).\
*   `realtime-js`\
    *   `RealtimeSubscription` class no longer exists and replaced by `RealtimeChannel`.\
    *   `RealtimeClient`'s `disconnect` method now returns type of `void` . It used to return type of `Promise<{ error: Error | null; data: boolean }`.\
    *   Removed `removeAllSubscriptions` and `removeSubscription` methods from `SupabaseClient` class.\
    *   Removed `SupabaseRealtimeClient` class.\
    *   Removed `SupabaseQueryBuilder` class.\
    *   Removed `SupabaseEventTypes` type.\
        *   Thinking about renaming this to something like `RealtimePostgresChangeEvents` and moving it to `realtime-js` v2.\
    *   Removed `.from(’table’).on(’INSERT’, () ⇒ {}).subscribe()` in favor of new Realtime client API.\
*   `functions-js`\
    *   supabase-js v1 only threw an error if the fetch call itself threw an error (network errors, etc) and not if the function returned HTTP errors like 400s or 500s. We have changed this behaviour to return an error if your function throws an error.\
    *   We have introduced new error types to distinguish between different kinds of errors. A `FunctionsHttpError` error is returned if your function throws an error, `FunctionsRelayError` if the Supabase Relay has an error processing your function and `FunctionsFetchError` if there is a network error in calling your function.\
    *   The correct content-type headers are automatically attached when sending the request if you don’t pass in a `Content-Type` header and pass in an argument to your function. We automatically attach the content type for `Blob`, `ArrayBuffer`, `File`, `FormData` ,`String` . If it doesn’t match any of these we assume the payload is `json` , we serialise the payload as JSON and attach the content type as `application/json`.\
    *   `responseType` does not need to be explicitly passed in. We parse the response based on the `Content-Type` response header sent by the function. We support parsing the responses as `text`, `json`, `blob`, `form-data` and are parsed as `text` by default.\
\
*   Need some help?\
    \
    [Contact support](https://supabase.com/support)\
    \
*   Latest product updates?\
    \
    [See Changelog](https://supabase.com/changelog)\
    \
*   Something's not right?\
    \
    [Check system status](https://status.supabase.com/)\
    \
\
* * *\
\
[© Supabase Inc](https://supabase.com/)\
—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)\
[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)\
[Open Source](https://supabase.com/open-source)\
[SupaSquad](https://supabase.com/supasquad)\
Privacy Settings\
\
[GitHub](https://github.com/supabase/supabase)\
[Twitter](https://twitter.com/supabase)\
[Discord](https://discord.supabase.com/)

# https://supabase.com/docs/reference/javascript/auth-api
[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

*   [Start](/docs/guides/getting-started)
    
*   Products
*   Build
*   Reference
*   Resources

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

Search docs...

K

Main menu

JavaScript

v2.0

*   [Introduction](/docs/reference/javascript/introduction)
    
*   [Installing](/docs/reference/javascript/installing)
    
*   [Initializing](/docs/reference/javascript/initializing)
    
*   [TypeScript support](/docs/reference/javascript/typescript-support)
    
*   * * *
    
    Database
    
    *   [Fetch data](/docs/reference/javascript/select)
        
    *   [Insert data](/docs/reference/javascript/insert)
        
    *   [Update data](/docs/reference/javascript/update)
        
    *   [Upsert data](/docs/reference/javascript/upsert)
        
    *   [Delete data](/docs/reference/javascript/delete)
        
    *   [Call a Postgres function](/docs/reference/javascript/rpc)
        
    *   Using filters
        
    *   Using modifiers
        
*   * * *
    
    Auth
    
    *   [Overview](/docs/reference/javascript/auth-api)
        
    *   [Error codes](/docs/reference/javascript/auth-error-codes)
        
    *   [Create a new user](/docs/reference/javascript/auth-signup)
        
    *   [Listen to auth events](/docs/reference/javascript/auth-onauthstatechange)
        
    *   [Create an anonymous user](/docs/reference/javascript/auth-signinanonymously)
        
    *   [Sign in a user](/docs/reference/javascript/auth-signinwithpassword)
        
    *   [Sign in with ID Token](/docs/reference/javascript/auth-signinwithidtoken)
        
    *   [Sign in a user through OTP](/docs/reference/javascript/auth-signinwithotp)
        
    *   [Sign in a user through OAuth](/docs/reference/javascript/auth-signinwithoauth)
        
    *   [Sign in a user through SSO](/docs/reference/javascript/auth-signinwithsso)
        
    *   [Sign out a user](/docs/reference/javascript/auth-signout)
        
    *   [Send a password reset request](/docs/reference/javascript/auth-resetpasswordforemail)
        
    *   [Verify and log in through OTP](/docs/reference/javascript/auth-verifyotp)
        
    *   [Retrieve a session](/docs/reference/javascript/auth-getsession)
        
    *   [Retrieve a new session](/docs/reference/javascript/auth-refreshsession)
        
    *   [Retrieve a user](/docs/reference/javascript/auth-getuser)
        
    *   [Update a user](/docs/reference/javascript/auth-updateuser)
        
    *   [Retrieve identities linked to a user](/docs/reference/javascript/auth-getuseridentities)
        
    *   [Link an identity to a user](/docs/reference/javascript/auth-linkidentity)
        
    *   [Unlink an identity from a user](/docs/reference/javascript/auth-unlinkidentity)
        
    *   [Send a password reauthentication nonce](/docs/reference/javascript/auth-reauthentication)
        
    *   [Resend an OTP](/docs/reference/javascript/auth-resend)
        
    *   [Set the session data](/docs/reference/javascript/auth-setsession)
        
    *   [Exchange an auth code for a session](/docs/reference/javascript/auth-exchangecodeforsession)
        
    *   [Start auto-refresh session (non-browser)](/docs/reference/javascript/auth-startautorefresh)
        
    *   [Stop auto-refresh session (non-browser)](/docs/reference/javascript/auth-stopautorefresh)
        
    *   Auth MFA
        
    *   Auth Admin
        
*   * * *
    
    Edge Functions
    
    *   [Invokes a Supabase Edge Function.](/docs/reference/javascript/functions-invoke)
        
*   * * *
    
    Realtime
    
    *   [Subscribe to channel](/docs/reference/javascript/subscribe)
        
    *   [Unsubscribe from a channel](/docs/reference/javascript/removechannel)
        
    *   [Unsubscribe from all channels](/docs/reference/javascript/removeallchannels)
        
    *   [Retrieve all channels](/docs/reference/javascript/getchannels)
        
    *   [Broadcast a message](/docs/reference/javascript/broadcastmessage)
        
*   * * *
    
    Storage
    
    *   [Create a bucket](/docs/reference/javascript/storage-createbucket)
        
    *   [Retrieve a bucket](/docs/reference/javascript/storage-getbucket)
        
    *   [List all buckets](/docs/reference/javascript/storage-listbuckets)
        
    *   [Update a bucket](/docs/reference/javascript/storage-updatebucket)
        
    *   [Delete a bucket](/docs/reference/javascript/storage-deletebucket)
        
    *   [Empty a bucket](/docs/reference/javascript/storage-emptybucket)
        
    *   [Upload a file](/docs/reference/javascript/storage-from-upload)
        
    *   [Download a file](/docs/reference/javascript/storage-from-download)
        
    *   [List all files in a bucket](/docs/reference/javascript/storage-from-list)
        
    *   [Replace an existing file](/docs/reference/javascript/storage-from-update)
        
    *   [Move an existing file](/docs/reference/javascript/storage-from-move)
        
    *   [Copy an existing file](/docs/reference/javascript/storage-from-copy)
        
    *   [Delete files in a bucket](/docs/reference/javascript/storage-from-remove)
        
    *   [Create a signed URL](/docs/reference/javascript/storage-from-createsignedurl)
        
    *   [Create signed URLs](/docs/reference/javascript/storage-from-createsignedurls)
        
    *   [Create signed upload URL](/docs/reference/javascript/storage-from-createsigneduploadurl)
        
    *   [Upload to a signed URL](/docs/reference/javascript/storage-from-uploadtosignedurl)
        
    *   [Retrieve public URL](/docs/reference/javascript/storage-from-getpublicurl)
        
*   * * *
    
    Misc
    
    *   [Release Notes](/docs/reference/javascript/release-notes)
        

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

*   [Start](/docs/guides/getting-started)
    
*   Products
*   Build
*   Reference
*   Resources

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)

Search docs...

K

Javascript Reference v2.0

JavaScript Client Library
=========================

@supabase/supabase-js[View on GitHub](https://github.com/supabase/supabase-js)

This reference documents every object and method available in Supabase's isomorphic JavaScript library, `supabase-js`. You can use `supabase-js` to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.

* * *

Installing
----------

### Install as package[#](#install-as-package)

You can install @supabase/supabase-js via the terminal.

npmYarnpnpm

Terminal

`     _10  npm install @supabase/supabase-js      `

### Install via CDN[#](#install-via-cdn)

You can install @supabase/supabase-js via CDN links.

`     _10  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>  _10  //or  _10  <script src="https://unpkg.com/@supabase/supabase-js@2"></script>      `

### Use at runtime in Deno[#](#use-at-runtime-in-deno)

You can use supabase-js in the Deno runtime via [JSR](https://jsr.io/@supabase/supabase-js)
:

`     _10  import { createClient } from 'jsr:@supabase/supabase-js@2'      `

* * *

Initializing
------------

Create a new client for use in the browser.

You can initialize a new Supabase client using the `createClient()` method.

The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything we offer within the Supabase ecosystem.

### Parameters

*   supabaseUrlRequiredstring
    
    The unique Supabase URL which is supplied when you create a new project in your project dashboard.
    
*   supabaseKeyRequiredstring
    
    The unique Supabase Key which is supplied when you create a new project in your project dashboard.
    
*   optionsOptionalSupabaseClientOptions
    
    Details
    

Creating a clientWith a custom domainWith additional parametersWith custom schemasCustom fetch implementationReact Native options with AsyncStorageReact Native options with Expo SecureStore

`     _10  import { createClient } from '@supabase/supabase-js'  _10  _10  // Create a single supabase client for interacting with your database  _10  const supabase = createClient('https://xyzcompany.supabase.co', 'public-anon-key')      `

* * *

TypeScript support
------------------

`supabase-js` has TypeScript support for type inference, autocompletion, type-safe queries, and more.

With TypeScript, `supabase-js` detects things like `not null` constraints and [generated columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html)
. Nullable columns are typed as `T | null` when you select the column. Generated columns will show a type error when you insert to it.

`supabase-js` also detects relationships between tables. A referenced table with one-to-many relationship is typed as `T[]`. Likewise, a referenced table with many-to-one relationship is typed as `T | null`.

Generating TypeScript Types[#](#generating-typescript-types)

-------------------------------------------------------------

You can use the Supabase CLI to [generate the types](/docs/reference/cli/supabase-gen-types)
. You can also generate the types [from the dashboard](https://supabase.com/dashboard/project/_/api?page=tables-intro)
.

Terminal

`     _10  supabase gen types typescript --project-id abcdefghijklmnopqrst > database.types.ts      `

These types are generated from your database schema. Given a table `public.movies`, the generated types will look like:

`     _10  create table public.movies (  _10  id bigint generated always as identity primary key,  _10  name text not null,  _10  data jsonb null  _10  );      `

./database.types.ts

``     _25  export type Json = string | number | boolean | null | { [key: string]: Json | undefined } | Json[]  _25  _25  export interface Database {  _25  public: {  _25  Tables: {  _25  movies: {  _25  Row: { // the data expected from .select()  _25  id: number  _25  name: string  _25  data: Json | null  _25  }  _25  Insert: { // the data to be passed to .insert()  _25  id?: never // generated columns must not be supplied  _25  name: string // `not null` columns with no default must be supplied  _25  data?: Json | null // nullable columns can be omitted  _25  }  _25  Update: { // the data to be passed to .update()  _25  id?: never  _25  name?: string // `not null` columns are optional on .update()  _25  data?: Json | null  _25  }  _25  }  _25  }  _25  }  _25  }      ``

Using TypeScript type definitions[#](#using-typescript-type-definitions)

-------------------------------------------------------------------------

You can supply the type definitions to `supabase-js` like so:

./index.tsx

`     _10  import { createClient } from '@supabase/supabase-js'  _10  import { Database } from './database.types'  _10  _10  const supabase = createClient<Database>(  _10  process.env.SUPABASE_URL,  _10  process.env.SUPABASE_ANON_KEY  _10  )      `

Helper types for Tables and Joins[#](#helper-types-for-tables-and-joins)

-------------------------------------------------------------------------

You can use the following helper types to make the generated TypeScript types easier to use.

Sometimes the generated types are not what you expect. For example, a view's column may show up as nullable when you expect it to be `not null`. Using [type-fest](https://github.com/sindresorhus/type-fest)
, you can override the types like so:

./database-generated.types.ts

`     _10  export type Json = // ...  _10  _10  export interface Database {  _10  // ...  _10  }      `

./database.types.ts

``     _20  import { MergeDeep } from 'type-fest'  _20  import { Database as DatabaseGenerated } from './database-generated.types'  _20  export { Json } from './database-generated.types'  _20  _20  // Override the type for a specific column in a view:  _20  export type Database = MergeDeep<  _20  DatabaseGenerated,  _20  {  _20  public: {  _20  Views: {  _20  movies_view: {  _20  Row: {  _20  // id is a primary key in public.movies, so it must be `not null`  _20  id: number  _20  }  _20  }  _20  }  _20  }  _20  }  _20  >      ``

You can also override the type of an individual successful response if needed:

`     _10  const { data } = await supabase.from('countries').select().returns<MyType>()      `

The generated types provide shorthands for accessing tables and enums.

./index.ts

`     _10  import { Database, Tables, Enums } from "./database.types.ts";  _10  _10  // Before 😕  _10  let movie: Database['public']['Tables']['movies']['Row'] = // ...  _10  _10  // After 😍  _10  let movie: Tables<'movies'>      `

### Response types for complex queries[#](#response-types-for-complex-queries)

`supabase-js` always returns a `data` object (for success), and an `error` object (for unsuccessful requests).

These helper types provide the result types from any query, including nested types for database joins.

Given the following schema with a relation between cities and countries, we can get the nested `CountriesWithCities` type:

`     _10  create table countries (  _10  "id" serial primary key,  _10  "name" text  _10  );  _10  _10  create table cities (  _10  "id" serial primary key,  _10  "name" text,  _10  "country_id" int references "countries"  _10  );      `

``     _17  import { QueryResult, QueryData, QueryError } from '@supabase/supabase-js'  _17  _17  const countriesWithCitiesQuery = supabase  _17  .from("countries")  _17  .select(`  _17  id,  _17  name,  _17  cities (  _17  id,  _17  name  _17  )  _17  `);  _17  type CountriesWithCities = QueryData<typeof countriesWithCitiesQuery>;  _17  _17  const { data, error } = await countriesWithCitiesQuery;  _17  if (error) throw error;  _17  const countriesWithCities: CountriesWithCities = data;      ``

* * *

Fetch data
----------

Perform a SELECT query on the table or view.

*   By default, Supabase projects return a maximum of 1,000 rows. This setting can be changed in your project's [API settings](/dashboard/project/_/settings/api)
    . It's recommended that you keep it low to limit the payload size of accidental or malicious requests. You can use `range()` queries to paginate through your data.
*   `select()` can be combined with [Filters](/docs/reference/javascript/using-filters)
    
*   `select()` can be combined with [Modifiers](/docs/reference/javascript/using-modifiers)
    
*   `apikey` is a reserved keyword if you're using the [Supabase Platform](/docs/guides/platform)
     and [should be avoided as a column name](https://github.com/supabase/supabase/issues/5465)
    .

### Parameters

*   columnsOptionalQuery
    
    The columns to retrieve, separated by commas. Columns can be renamed when returned with `customName:columnName`
    
*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Getting your dataSelecting specific columnsQuery referenced tablesQuery referenced tables through a join tableQuery the same referenced table multiple timesFiltering through referenced tablesQuerying referenced table with countQuerying with count optionQuerying JSON dataQuerying referenced table with inner joinSwitching schemas per query

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()      `

Data source

Response

* * *

Insert data
-----------

Perform an INSERT into the table or view.

### Parameters

*   valuesRequiredUnion: expand to see options
    
    The values to insert. Pass an object to insert a single row or an array to insert multiple rows.
    
    Details
    
*   optionsOptionalobject
    
    Named parameters
    
    Details
    

Create a recordCreate a record and return itBulk create

`     _10  const { error } = await supabase  _10  .from('countries')  _10  .insert({ id: 1, name: 'Denmark' })      `

Data source

Response

* * *

Update data
-----------

Perform an UPDATE on the table or view.

*   `update()` should always be combined with [Filters](/docs/reference/javascript/using-filters)
     to target the item(s) you wish to update.

### Parameters

*   valuesRequiredRow
    
    The values to update with
    
*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Updating your dataUpdate a record and return itUpdating JSON data

`     _10  const { error } = await supabase  _10  .from('countries')  _10  .update({ name: 'Australia' })  _10  .eq('id', 1)      `

Data source

Response

* * *

Upsert data
-----------

Perform an UPSERT on the table or view. Depending on the column(s) passed to `onConflict`, `.upsert()` allows you to perform the equivalent of `.insert()` if a row with the corresponding `onConflict` columns doesn't exist, or if it does exist, perform an alternative action depending on `ignoreDuplicates`.

*   Primary keys must be included in `values` to use upsert.

### Parameters

*   valuesRequiredUnion: expand to see options
    
    The values to upsert with. Pass an object to upsert a single row or an array to upsert multiple rows.
    
    Details
    
*   optionsOptionalobject
    
    Named parameters
    
    Details
    

Upsert your dataBulk Upsert your dataUpserting into tables with constraints

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .upsert({ id: 1, name: 'Albania' })  _10  .select()      `

Data source

Response

* * *

Delete data
-----------

Perform a DELETE on the table or view.

*   `delete()` should always be combined with [filters](/docs/reference/javascript/using-filters)
     to target the item(s) you wish to delete.
*   If you use `delete()` with filters and you have [RLS](/docs/learn/auth-deep-dive/auth-row-level-security)
     enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/`ALL` policy that makes the rows visible.
*   When using `delete().in()`, specify an array of values to target multiple rows with a single query. This is particularly useful for batch deleting entries that share common criteria, such as deleting users by their IDs. Ensure that the array you provide accurately represents all records you intend to delete to avoid unintended data removal.

### Parameters

*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Delete a single recordDelete a record and return itDelete multiple records

`     _10  const response = await supabase  _10  .from('countries')  _10  .delete()  _10  .eq('id', 1)      `

Data source

Response

* * *

Call a Postgres function
------------------------

Perform a function call.

You can call Postgres functions as _Remote Procedure Calls_, logic in your database that you can execute from anywhere. Functions are useful when the logic rarely changes—like for password resets and updates.

`     _10  create or replace function hello_world() returns text as $$  _10  select 'Hello world';  _10  $$ language sql;      `

To call Postgres functions on [Read Replicas](/docs/guides/platform/read-replicas)
, use the `get: true` option.

### Parameters

*   fnRequiredFnName
    
    The function name to call
    
*   argsRequiredFn\['Args'\]
    
    The arguments to pass to the function call
    
*   optionsRequiredobject
    
    Named parameters
    
    Details
    

Call a Postgres function without argumentsCall a Postgres function with argumentsBulk processingCall a Postgres function with filtersCall a read-only Postgres function

`     _10  const { data, error } = await supabase.rpc('hello_world')      `

Data source

Response

* * *

Using filters
-------------

Filters allow you to only return rows that match certain conditions.

Filters can be used on `select()`, `update()`, `upsert()`, and `delete()` queries.

If a Postgres function returns a table response, you can also apply filters.

Applying FiltersChainingConditional ChainingFilter by values within a JSON columnFilter referenced tables

`     _10  const { data, error } = await supabase  _10  .from('cities')  _10  .select('name, country_id')  _10  .eq('name', 'The Shire') // Correct  _10  _10  const { data, error } = await supabase  _10  .from('cities')  _10  .eq('name', 'The Shire') // Incorrect  _10  .select('name, country_id')      `

Notes

* * *

Column is equal to a value
--------------------------

Match only rows where `column` is equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredNonNullable
    
    The value to filter with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .eq('name', 'Albania')      `

Data source

Response

* * *

Column is not equal to a value
------------------------------

Match only rows where `column` is not equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .neq('name', 'Albania')      `

Data source

Response

* * *

Column is greater than a value
------------------------------

Match only rows where `column` is greater than `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .gt('id', 2)      `

Data source

Response

Notes

* * *

Column is greater than or equal to a value
------------------------------------------

Match only rows where `column` is greater than or equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .gte('id', 2)      `

Data source

Response

* * *

Column is less than a value
---------------------------

Match only rows where `column` is less than `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .lt('id', 2)      `

Data source

Response

* * *

Column is less than or equal to a value
---------------------------------------

Match only rows where `column` is less than or equal to `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .lte('id', 2)      `

Data source

Response

* * *

Column matches a pattern
------------------------

Match only rows where `column` matches `pattern` case-sensitively.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   patternRequiredstring
    
    The pattern to match with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .like('name', '%Alba%')      `

Data source

Response

* * *

Column matches a case-insensitive pattern
-----------------------------------------

Match only rows where `column` matches `pattern` case-insensitively.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   patternRequiredstring
    
    The pattern to match with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .ilike('name', '%alba%')      `

Data source

Response

* * *

Column is a value
-----------------

Match only rows where `column` IS `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The value to filter with
    
    Details
    

Checking for nullness, true or false

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .is('name', null)      `

Data source

Response

Notes

* * *

Column is in an array
---------------------

Match only rows where `column` is included in the `values` array.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The column to filter on
    
    Details
    
*   valuesRequiredArray<Row\['ColumnName'\]>
    
    The values array to filter with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .in('name', ['Albania', 'Algeria'])      `

Data source

Response

* * *

Column contains every element in a value
----------------------------------------

Only relevant for jsonb, array, and range columns. Match only rows where `column` contains every element appearing in `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The jsonb, array, or range column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The jsonb, array, or range value to filter with
    
    Details
    

On array columnsOn range columnsOn \`jsonb\` columns

`     _10  const { data, error } = await supabase  _10  .from('issues')  _10  .select()  _10  .contains('tags', ['is:open', 'priority:low'])      `

Data source

Response

* * *

Contained by value
------------------

Only relevant for jsonb, array, and range columns. Match only rows where every element appearing in `column` is contained by `value`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The jsonb, array, or range column to filter on
    
    Details
    
*   valueRequiredUnion: expand to see options
    
    The jsonb, array, or range value to filter with
    
    Details
    

On array columnsOn range columnsOn \`jsonb\` columns

`     _10  const { data, error } = await supabase  _10  .from('classes')  _10  .select('name')  _10  .containedBy('days', ['monday', 'tuesday', 'wednesday', 'friday'])      `

Data source

Response

* * *

Greater than a range
--------------------

Only relevant for range columns. Match only rows where every element in `column` is greater than any element in `range`.

### Parameters

*   columnRequiredUnion: expand to see options
    
    The range column to filter on
    
    Details
    
*   rangeRequiredstring
    
    The range to filter with
    

With \`select()\`

`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeGt('during', '[2000-01-02 08:00, 2000-01-02 09:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Greater than or equal to a range\
--------------------------------\
\
Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or greater than any element in `range`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeGte('during', '[2000-01-02 08:30, 2000-01-02 09:30)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Less than a range\
-----------------\
\
Only relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeLt('during', '[2000-01-01 15:00, 2000-01-01 16:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Less than or equal to a range\
-----------------------------\
\
Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or less than any element in `range`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeLte('during', '[2000-01-01 14:00, 2000-01-01 16:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Mutually exclusive to a range\
-----------------------------\
\
Only relevant for range columns. Match only rows where `column` is mutually exclusive to `range` and there can be no element between the two ranges.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The range column to filter on\
    \
    Details\
    \
*   rangeRequiredstring\
    \
    The range to filter with\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('reservations')  _10  .select()  _10  .rangeAdjacent('during', '[2000-01-01 12:00, 2000-01-01 13:00)')      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
With a common element\
---------------------\
\
Only relevant for array and range columns. Match only rows where `column` and `value` have an element in common.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The array or range column to filter on\
    \
    Details\
    \
*   valueRequiredUnion: expand to see options\
    \
    The array or range value to filter with\
    \
    Details\
    \
\
On array columnsOn range columns\
\
`     _10  const { data, error } = await supabase  _10  .from('issues')  _10  .select('title')  _10  .overlaps('tags', ['is:closed', 'severity:high'])      `\
\
Data source\
\
Response\
\
* * *\
\
Match a string\
--------------\
\
Only relevant for text and tsvector columns. Match only rows where `column` matches the query string in `query`.\
\
*   For more information, see [Postgres full text search](/docs/guides/database/full-text-search)\
    .\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The text or tsvector column to filter on\
    \
    Details\
    \
*   queryRequiredstring\
    \
    The query text to match with\
    \
*   optionsOptionalobject\
    \
    Named parameters\
    \
    Details\
    \
\
Text searchBasic normalizationFull normalizationWebsearch\
\
``     _10  const result = await supabase  _10  .from("texts")  _10  .select("content")  _10  .textSearch("content", `'eggs' & 'ham'`, {  _10  config: "english",  _10  });      ``\
\
Data source\
\
Response\
\
* * *\
\
Match an associated value\
-------------------------\
\
Match only rows where each column in `query` keys is equal to its associated value. Shorthand for multiple `.eq()`s.\
\
### Parameters\
\
*   queryRequiredUnion: expand to see options\
    \
    The object to filter with, with column names as keys mapped to their filter values\
    \
    Details\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .match({ id: 2, name: 'Albania' })      `\
\
Data source\
\
Response\
\
* * *\
\
Don't match the filter\
----------------------\
\
Match only rows which doesn't satisfy the filter.\
\
not() expects you to use the raw PostgREST syntax for the filter values.\
\
``     _10  .not('id', 'in', '(5,6,7)') // Use `()` for `in` filter  _10  .not('arraycol', 'cs', '\{"a","b"\}') // Use `cs` for `contains()`, `\{\}` for array values      ``\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The column to filter on\
    \
    Details\
    \
*   operatorRequiredUnion: expand to see options\
    \
    The operator to be negated to filter with, following PostgREST syntax\
    \
    Details\
    \
*   valueRequiredUnion: expand to see options\
    \
    The value to filter with, following PostgREST syntax\
    \
    Details\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .not('name', 'is', null)      `\
\
Data source\
\
Response\
\
* * *\
\
Match at least one filter\
-------------------------\
\
Match only rows which satisfy at least one of the filters.\
\
or() expects you to use the raw PostgREST syntax for the filter names and values.\
\
``     _10  .or('id.in.(5,6,7), arraycol.cs.\{"a","b"\}') // Use `()` for `in` filter, `\{\}` for array values and `cs` for `contains()`.  _10  .or('id.in.(5,6,7), arraycol.cd.\{"a","b"\}') // Use `cd` for `containedBy()`      ``\
\
### Parameters\
\
*   filtersRequiredstring\
    \
    The filters to use, following PostgREST syntax\
    \
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`Use \`or\` with \`and\`Use \`or\` on referenced tables\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .or('id.eq.2,name.eq.Algeria')      `\
\
Data source\
\
Response\
\
* * *\
\
Match the filter\
----------------\
\
Match only rows which satisfy the filter. This is an escape hatch - you should use the specific filter methods wherever possible.\
\
filter() expects you to use the raw PostgREST syntax for the filter values.\
\
``     _10  .filter('id', 'in', '(5,6,7)') // Use `()` for `in` filter  _10  .filter('arraycol', 'cs', '\{"a","b"\}') // Use `cs` for `contains()`, `\{\}` for array values      ``\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The column to filter on\
    \
    Details\
    \
*   operatorRequiredUnion: expand to see options\
    \
    The operator to filter with, following PostgREST syntax\
    \
    Details\
    \
*   valueRequiredunknown\
    \
    The value to filter with, following PostgREST syntax\
    \
\
With \`select()\`On a referenced table\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .filter('name', 'in', '("Algeria","Japan")')      `\
\
Data source\
\
Response\
\
* * *\
\
Using modifiers\
---------------\
\
Filters work on the row level—they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition—allowing you to change the format of the response (e.g., returning a CSV string).\
\
Modifiers must be specified after filters. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).\
\
* * *\
\
Return data after inserting\
---------------------------\
\
Perform a SELECT on the query result.\
\
### Parameters\
\
*   columnsOptionalQuery\
    \
    The columns to retrieve, separated by commas\
    \
\
With \`upsert()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .upsert({ id: 1, name: 'Algeria' })  _10  .select()      `\
\
Data source\
\
Response\
\
* * *\
\
Order the results\
-----------------\
\
Order the query result by `column`.\
\
### Parameters\
\
*   columnRequiredUnion: expand to see options\
    \
    The column to order by\
    \
    Details\
    \
*   optionsOptionalobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`On a referenced table\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('id', 'name')  _10  .order('id', { ascending: false })      `\
\
Data source\
\
Response\
\
* * *\
\
Limit the number of rows returned\
---------------------------------\
\
Limit the query result by `count`.\
\
### Parameters\
\
*   countRequirednumber\
    \
    The maximum number of rows to return\
    \
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`On a referenced table\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .limit(1)      `\
\
Data source\
\
Response\
\
* * *\
\
Limit the query to a range\
--------------------------\
\
Limit the query result by starting at an offset (`from`) and ending at the offset (`from + to`). Only records within this range are returned. This respects the query order and if there is no order clause the range could behave unexpectedly. The `from` and `to` values are 0-based and inclusive: `range(1, 3)` will include the second, third and fourth rows of the query.\
\
### Parameters\
\
*   fromRequirednumber\
    \
    The starting index from which to limit the result\
    \
*   toRequirednumber\
    \
    The last index to which to limit the result\
    \
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .range(0, 1)      `\
\
Data source\
\
Response\
\
* * *\
\
Set an abort signal\
-------------------\
\
Set the AbortSignal for the fetch request.\
\
You can use this to set a timeout for the request.\
\
### Parameters\
\
*   signalRequiredAbortSignal\
    \
    The AbortSignal to use for the fetch request\
    \
\
Aborting requests in-flightSet a timeout\
\
`     _10  const ac = new AbortController()  _10  ac.abort()  _10  const { data, error } = await supabase  _10  .from('very_big_table')  _10  .select()  _10  .abortSignal(ac.signal)      `\
\
Response\
\
Notes\
\
* * *\
\
Retrieve one row of data\
------------------------\
\
Return `data` as a single object instead of an array of objects.\
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select('name')  _10  .limit(1)  _10  .single()      `\
\
Data source\
\
Response\
\
* * *\
\
Retrieve zero or one row of data\
--------------------------------\
\
Return `data` as a single object instead of an array of objects.\
\
### Return Type\
\
Union: expand to see options\
\
Details\
\
With \`select()\`\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .eq('name', 'Singapore')  _10  .maybeSingle()      `\
\
Data source\
\
Response\
\
* * *\
\
Retrieve as a CSV\
-----------------\
\
Return `data` as a string in CSV format.\
\
### Return Type\
\
string\
\
Return data as CSV\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .csv()      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Override type of successful response\
------------------------------------\
\
Override the type of the returned `data`.\
\
Override type of successful response\
\
`     _10  const { data } = await supabase  _10  .from('countries')  _10  .select()  _10  .returns<MyType>()      `\
\
Response\
\
* * *\
\
Using explain\
-------------\
\
Return `data` as the EXPLAIN plan for the query.\
\
For debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html)\
 of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.\
\
Explain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.\
\
Follow the [Performance Debugging Guide](/docs/guides/database/debugging-performance)\
 to enable the functionality on your project.\
\
### Parameters\
\
*   optionsRequiredobject\
    \
    Named parameters\
    \
    Details\
    \
\
### Return Type\
\
Union: expand to see options\
\
Details\
\
Get the execution planGet the execution plan with analyze and verbose\
\
`     _10  const { data, error } = await supabase  _10  .from('countries')  _10  .select()  _10  .explain()      `\
\
Data source\
\
Response\
\
Notes\
\
* * *\
\
Overview\
--------\
\
*   The auth methods can be accessed via the `supabase.auth` namespace.\
    \
*   By default, the supabase client sets `persistSession` to true and attempts to store the session in local storage. When using the supabase client in an environment that doesn't support local storage, you might notice the following warning message being logged:\
    \
    > No storage option exists to persist the session, which may result in unexpected behavior when using auth. If you want to set `persistSession` to true, please provide a storage option or you may set `persistSession` to false to disable this warning.\
    \
    This warning message can be safely ignored if you're not using auth on the server-side. If you are using auth and you want to set `persistSession` to true, you will need to provide a custom storage implementation that follows [this interface](https://github.com/supabase/gotrue-js/blob/master/src/lib/types.ts#L1027)\
    .\
    \
*   Any email links and one-time passwords (OTPs) sent have a default expiry of 24 hours. We have the following [rate limits](/docs/guides/platform/going-into-prod#auth-rate-limits)\
     in place to guard against brute force attacks.\
    \
*   The expiry of an access token can be set in the "JWT expiry limit" field in [your project's auth settings](/dashboard/project/_/settings/auth)\
    . A refresh token never expires and can only be used once.\
    \
\
Create auth clientCreate auth client (server-side)\
\
`     _10  import { createClient } from '@supabase/supabase-js'  _10  _10  const supabase = createClient(supabase_url, anon_key)      `\
\
* * *\
\
Error codes\
-----------\
\
Supabase Auth can throw or return various errors when using the API. All errors originating from the `supabase.auth` namespace of the client library will be wrapped by the `AuthError` class.\
\
Error objects are split in a few classes:\
\
*   `AuthApiError` -- errors which originate from the Supabase Auth API.\
    *   Use `isAuthApiError` instead of `instanceof` checks to see if an error you caught is of this type.\
*   `CustomAuthError` -- errors which generally originate from state in the client library.\
    *   Use the `name` property on the error to identify the class of error received.\
\
Errors originating from the server API classed as `AuthApiError` always have a `code` property that can be used to identify the error returned by the server. The `status` property is also present, encoding the HTTP status code received in the response.\
\
In general the HTTP status codes you will likely receive are:\
\
*   [403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403)\
     is sent out in rare situations where a certain Auth feature is not available for the user, and you as the developer are not checking a precondition whether that API is available for the user.\
*   [422 Unprocessable Entity](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422)\
     is sent out when the API request is accepted, but cannot be processed because the user or Auth server is in a state where it cannot satisfy the request.\
*   [429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)\
     is sent out when rate-limits are breached for an API. You should handle this status code often, especially in functions that authenticate a user.\
*   [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)\
     often means that the Auth server's service is degraded. Most often it points to issues in your database setup such as a misbehaving trigger on a schema, function, view or other database object.\
*   [501 Not Implemented](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501)\
     is sent out when a feature is not enabled on the Auth server, and you are trying to use an API which requires it.\
\
To supplement HTTP status codes, Supabase Auth returns a string error code which gives you more insight into what went wrong. These codes are stable and can be used to present an internationalized message to your users.\
\
| Code | Description |\
| --- | --- |\
| `anonymous_provider_disabled` | Anonymous sign-ins are disabled. |\
| `bad_code_verifier` | Returned from the PKCE flow where the provided code verifier does not match the expected one. Indicates a bug in the implementation of the client library. |\
| `bad_json` | Usually used when the HTTP body of the request is not valid JSON. |\
| `bad_jwt` | JWT sent in the `Authorization` header is not valid. |\
| `bad_oauth_callback` | OAuth callback from provider to Auth does not have all the required attributes (state). Indicates an issue with the OAuth provider or client library implementation. |\
| `bad_oauth_state` | OAuth state (data echoed back by the OAuth provider to Supabase Auth) is not in the correct format. Indicates an issue with the OAuth provider integration. |\
| `captcha_failed` | Captcha challenge could not be verified with the captcha provider. Check your captcha integration. |\
| `conflict` | General database conflict, such as concurrent requests on resources that should not be modified concurrently. Can often occur when you have too many session refresh requests firing off at the same time for a user. Check your app for concurrency issues, and if detected, back off exponentially. |\
| `email_conflict_identity_not_deletable` | Unlinking this identity causes the user's account to change to an email address which is already used by another user account. Indicates an issue where the user has two different accounts using different primary email addresses. You may need to migrate user data to one of their accounts in this case. |\
| `email_exists` | Email address already exists in the system. |\
| `email_not_confirmed` | Signing in is not allowed for this user as the email address is not confirmed. |\
| `email_provider_disabled` | Signups are disabled for email and password. |\
| `flow_state_expired` | PKCE flow state to which the API request relates has expired. Ask the user to sign in again. |\
| `flow_state_not_found` | PKCE flow state to which the API request relates no longer exists. Flow states expire after a while and are progressively cleaned up, which can cause this error. Retried requests can cause this error, as the previous request likely destroyed the flow state. Ask the user to sign in again. |\
| `hook_payload_over_size_limit` | Payload from Auth exceeds maximum size limit. |\
| `hook_timeout` | Unable to reach hook within maximum time allocated. |\
| `hook_timeout_after_retry` | Unable to reach hook after maximum number of retries. |\
| `identity_already_exists` | The identity to which the API relates is already linked to a user. |\
| `identity_not_found` | Identity to which the API call relates does not exist, such as when an identity is unlinked or deleted. |\
| `insufficient_aal` | To call this API, the user must have a higher [Authenticator Assurance Level](https://supabase.com/docs/guides/auth/auth-mfa)<br>. To resolve, ask the user to solve an MFA challenge. |\
| `invite_not_found` | Invite is expired or already used. |\
| `invalid_credentials` | Login credentials or grant type not recognized. |\
| `manual_linking_disabled` | Calling the `supabase.auth.linkUser()` and related APIs is not enabled on the Auth server. |\
| `mfa_challenge_expired` | Responding to an MFA challenge should happen within a fixed time period. Request a new challenge when encountering this error. |\
| `mfa_factor_name_conflict` | MFA factors for a single user should not have the same friendly name. |\
| `mfa_factor_not_found` | MFA factor no longer exists. |\
| `mfa_ip_address_mismatch` | The enrollment process for MFA factors must begin and end with the same IP address. |\
| `mfa_verification_failed` | MFA challenge could not be verified -- wrong TOTP code. |\
| `mfa_verification_rejected` | Further MFA verification is rejected. Only returned if the [MFA verification attempt hook](https://supabase.com/docs/guides/auth/auth-hooks?language=add-admin-role#hook-mfa-verification-attempt)<br> returns a reject decision. |\
| `mfa_verified_factor_exists` | Verified phone factor already exists for a user. Unenroll existing verified phone factor to continue. |\
| `mfa_totp_enroll_disabled` | Enrollment of MFA TOTP factors is disabled. |\
| `mfa_totp_verify_disabled` | Login via TOTP factors and verification of new TOTP factors is disabled. |\
| `mfa_phone_enroll_disabled` | Enrollment of MFA Phone factors is disabled. |\
| `mfa_phone_verify_disabled` | Login via Phone factors and verification of new Phone factors is disabled. |\
| `no_authorization` | This HTTP request requires an `Authorization` header, which is not provided. |\
| `not_admin` | User accessing the API is not admin, i.e. the JWT does not contain a `role` claim that identifies them as an admin of the Auth server. |\
| `oauth_provider_not_supported` | Using an OAuth provider which is disabled on the Auth server. |\
| `otp_disabled` | Sign in with OTPs (magic link, email OTP) is disabled. Check your sever's configuration. |\
| `otp_expired` | OTP code for this sign-in has expired. Ask the user to sign in again. |\
| `over_email_send_rate_limit` | Too many emails have been sent to this email address. Ask the user to wait a while before trying again. |\
| `over_request_rate_limit` | Too many requests have been sent by this client (IP address). Ask the user to try again in a few minutes. Sometimes can indicate a bug in your application that mistakenly sends out too many requests (such as a badly written [`useEffect` React hook](https://react.dev/reference/react/useEffect)<br>). |\
| `over_sms_send_rate_limit` | Too many SMS messages have been sent to this phone number. Ask the user to wait a while before trying again. |\
| `phone_exists` | Phone number already exists in the system. |\
| `phone_not_confirmed` | Signing in is not allowed for this user as the phone number is not confirmed. |\
| `phone_provider_disabled` | Signups are disabled for phone and password. |\
| `provider_disabled` | OAuth provider is disabled for use. Check your server's configuration. |\
| `provider_email_needs_verification` | Not all OAuth providers verify their user's email address. Supabase Auth requires emails to be verified, so this error is sent out when a verification email is sent after completing the OAuth flow. |\
| `reauthentication_needed` | A user needs to reauthenticate to change their password. Ask the user to reauthenticate by calling the `supabase.auth.reauthenticate()` API. |\
| `reauthentication_not_valid` | Verifying a reauthentication failed, the code is incorrect. Ask the user to enter a new code. |\
| `request_timeout` | Processing the request took too long. Retry the request. |\
| `same_password` | A user that is updating their password must use a different password than the one currently used. |\
| `saml_assertion_no_email` | SAML assertion (user information) was received after sign in, but no email address was found in it, which is required. Check the provider's attribute mapping and/or configuration. |\
| `saml_assertion_no_user_id` | SAML assertion (user information) was received after sign in, but a user ID (called NameID) was not found in it, which is required. Check the SAML identity provider's configuration. |\
| `saml_entity_id_mismatch` | (Admin API.) Updating the SAML metadata for a SAML identity provider is not possible, as the entity ID in the update does not match the entity ID in the database. This is equivalent to creating a new identity provider, and you should do that instead. |\
| `saml_idp_already_exists` | (Admin API.) Adding a SAML identity provider that is already added. |\
| `saml_idp_not_found` | SAML identity provider not found. Most often returned after IdP-initiated sign-in with an unregistered SAML identity provider in Supabase Auth. |\
| `saml_metadata_fetch_failed` | (Admin API.) Adding or updating a SAML provider failed as its metadata could not be fetched from the provided URL. |\
| `saml_provider_disabled` | Using [Enterprise SSO with SAML 2.0](https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml)<br> is not enabled on the Auth server. |\
| `saml_relay_state_expired` | SAML relay state is an object that tracks the progress of a `supabase.auth.signInWithSSO()` request. The SAML identity provider should respond after a fixed amount of time, after which this error is shown. Ask the user to sign in again. |\
| `saml_relay_state_not_found` | SAML relay states are progressively cleaned up after they expire, which can cause this error. Ask the user to sign in again. |\
| `session_not_found` | Session to which the API request relates no longer exists. This can occur if the user has signed out, or the session entry in the database was deleted in some other way. |\
| `signup_disabled` | Sign ups (new account creation) are disabled on the server. |\
| `single_identity_not_deletable` | Every user must have at least one identity attached to it, so deleting (unlinking) an identity is not allowed if it's the only one for the user. |\
| `sms_send_failed` | Sending an SMS message failed. Check your SMS provider configuration. |\
| `sso_domain_already_exists` | (Admin API.) Only one SSO domain can be registered per SSO identity provider. |\
| `sso_provider_not_found` | SSO provider not found. Check the arguments in `supabase.auth.signInWithSSO()`. |\
| `too_many_enrolled_mfa_factors` | A user can only have a fixed number of enrolled MFA factors. |\
| `unexpected_audience` | (Deprecated feature not available via Supabase client libraries.) The request's `X-JWT-AUD` claim does not match the JWT's audience. |\
| `unexpected_failure` | Auth service is degraded or a bug is present, without a specific reason. |\
| `user_already_exists` | User with this information (email address, phone number) cannot be created again as it already exists. |\
| `user_banned` | User to which the API request relates has a `banned_until` property which is still active. No further API requests should be attempted until this field is cleared. |\
| `user_not_found` | User to which the API request relates no longer exists. |\
| `user_sso_managed` | When a user comes from SSO, certain fields of the user cannot be updated (like `email`). |\
| `validation_failed` | Provided parameters are not in the expected format. |\
| `weak_password` | User is signing up or changing their password without meeting the password strength criteria. Use the `AuthWeakPasswordError` class to access more information about what they need to do to make the password pass. |\
\
### Tips for better error handling[#](#tips-for-better-error-handling)\
\
*   Do not use string matching on error messages! Always use the `name` and `code` properties of error objects to identify the situation.\
*   Although HTTP status codes generally don't change, they can suddenly change due to bugs, so avoid relying on them unless absolutely necessary.\
\
* * *\
\
Create a new user\
-----------------\
\
Creates a new user.\
\
*   By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](/dashboard/project/_/auth/providers)\
    .\
*   **Confirm email** determines if users need to confirm their email address after signing up.\
    *   If **Confirm email** is enabled, a `user` is returned but `session` is null.\
    *   If **Confirm email** is disabled, both a `user` and a `session` are returned.\
*   When the user confirms their email address, they are redirected to the [`SITE_URL`](/docs/guides/auth/redirect-urls)\
     by default. You can modify your `SITE_URL` or add additional redirect URLs in [your project](/dashboard/project/_/auth/url-configuration)\
    .\
*   If signUp() is called for an existing confirmed user:\
    *   When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](/dashboard/project/_/auth/providers)\
        , an obfuscated/fake user object is returned.\
    *   When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.\
*   To fetch the currently logged-in user, refer to [`getUser()`](/docs/reference/javascript/auth-getuser)\
    .\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign up with an email and passwordSign up with a phone number and password (SMS)Sign up with a phone number and password (whatsapp)Sign up with additional user metadataSign up with a redirect URL\
\
`     _10  const { data, error } = await supabase.auth.signUp({  _10  email: 'example@email.com',  _10  password: 'example-password',  _10  })      `\
\
Response\
\
* * *\
\
Listen to auth events\
---------------------\
\
Receive a notification every time an auth event happens.\
\
*   Subscribes to important events occurring on the user's session.\
*   Use on the frontend/client. It is less useful on the server.\
*   Events are emitted across tabs to keep your application's UI up-to-date. Some events can fire very frequently, based on the number of tabs open. Use a quick and efficient callback function, and defer or debounce as many operations as you can to be performed outside of the callback.\
*   **Important:** A callback can be an `async` function and it runs synchronously during the processing of the changes causing the event. You can easily create a dead-lock by using `await` on a call to another method of the Supabase library.\
    *   Avoid using `async` functions as callbacks.\
    *   Limit the number of `await` calls in `async` callbacks.\
    *   Do not use other Supabase functions in the callback function. If you must, dispatch the functions once the callback has finished executing. Use this as a quick way to achieve this:\
        \
        `     _10  supabase.auth.onAuthStateChange((event, session) => \{  _10  setTimeout(async () => \{  _10  // await on other Supabase function here  _10  // this runs right after the callback has finished  _10  \}, 0)  _10  \})      `\
        \
*   Emitted events:\
    *   `INITIAL_SESSION`\
        *   Emitted right after the Supabase client is constructed and the initial session from storage is loaded.\
    *   `SIGNED_IN`\
        *   Emitted each time a user session is confirmed or re-established, including on user sign in and when refocusing a tab.\
        *   Avoid making assumptions as to when this event is fired, this may occur even when the user is already signed in. Instead, check the user object attached to the event to see if a new user has signed in and update your application's UI.\
        *   This event can fire very frequently depending on the number of tabs open in your application.\
    *   `SIGNED_OUT`\
        *   Emitted when the user signs out. This can be after:\
            *   A call to `supabase.auth.signOut()`.\
            *   After the user's session has expired for any reason:\
                *   User has signed out on another device.\
                *   The session has reached its timebox limit or inactivity timeout.\
                *   User has signed in on another device with single session per user enabled.\
                *   Check the [User Sessions](/docs/guides/auth/sessions)\
                     docs for more information.\
        *   Use this to clean up any local storage your application has associated with the user.\
    *   `TOKEN_REFRESHED`\
        *   Emitted each time a new access and refresh token are fetched for the signed in user.\
        *   It's best practice and highly recommended to extract the access token (JWT) and store it in memory for further use in your application.\
            *   Avoid frequent calls to `supabase.auth.getSession()` for the same purpose.\
        *   There is a background process that keeps track of when the session should be refreshed so you will always receive valid tokens by listening to this event.\
        *   The frequency of this event is related to the JWT expiry limit configured on your project.\
    *   `USER_UPDATED`\
        *   Emitted each time the `supabase.auth.updateUser()` method finishes successfully. Listen to it to update your application's UI based on new profile information.\
    *   `PASSWORD_RECOVERY`\
        *   Emitted instead of the `SIGNED_IN` event when the user lands on a page that includes a password recovery link in the URL.\
        *   Use it to show a UI to the user where they can [reset their password](/docs/guides/auth/passwords#resetting-a-users-password-forgot-password)\
            .\
\
### Parameters\
\
*   callbackRequiredfunction\
    \
    A callback function to be invoked when an auth event happens.\
    \
    Details\
    \
\
### Return Type\
\
object\
\
Details\
\
Listen to auth changesListen to sign outStore OAuth provider tokens on sign inUse React Context for the User's sessionListen to password recovery eventsListen to sign inListen to token refreshListen to user updates\
\
`     _20  const { data } = supabase.auth.onAuthStateChange((event, session) => {  _20  console.log(event, session)  _20  _20  if (event === 'INITIAL_SESSION') {  _20  // handle initial session  _20  } else if (event === 'SIGNED_IN') {  _20  // handle sign in event  _20  } else if (event === 'SIGNED_OUT') {  _20  // handle sign out event  _20  } else if (event === 'PASSWORD_RECOVERY') {  _20  // handle password recovery event  _20  } else if (event === 'TOKEN_REFRESHED') {  _20  // handle token refreshed event  _20  } else if (event === 'USER_UPDATED') {  _20  // handle user updated event  _20  }  _20  })  _20  _20  // call unsubscribe to remove the callback  _20  data.subscription.unsubscribe()      `\
\
* * *\
\
Create an anonymous user\
------------------------\
\
Creates a new anonymous user.\
\
*   Returns an anonymous user\
*   It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.\
\
### Parameters\
\
*   credentialsOptionalSignInAnonymouslyCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create an anonymous userCreate an anonymous user with custom user metadata\
\
`     _10  const { data, error } = await supabase.auth.signInAnonymously({  _10  options: {  _10  captchaToken  _10  }  _10  });      `\
\
Response\
\
* * *\
\
Sign in a user\
--------------\
\
Log in an existing user with an email and password or phone and password.\
\
*   Requires either an email and password or a phone number and password.\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in with email and passwordSign in with phone and password\
\
`     _10  const { data, error } = await supabase.auth.signInWithPassword({  _10  email: 'example@email.com',  _10  password: 'example-password',  _10  })      `\
\
Response\
\
* * *\
\
Sign in with ID Token\
---------------------\
\
Allows signing in with an OIDC ID token. The authentication provider used should be enabled and configured.\
\
### Parameters\
\
*   credentialsRequiredSignInWithIdTokenCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign In using ID Token\
\
`     _10  const { data, error } = await supabase.auth.signInWithIdToken({  _10  provider: 'google',  _10  token: 'your-id-token'  _10  })      `\
\
Response\
\
* * *\
\
Sign in a user through OTP\
--------------------------\
\
Log in a user using magiclink or a one-time password (OTP).\
\
*   Requires either an email or phone number.\
*   This method is used for passwordless sign-ins where a OTP is sent to the user's email or phone number.\
*   If the user doesn't exist, `signInWithOtp()` will signup the user instead. To restrict this behavior, you can set `shouldCreateUser` in `SignInWithPasswordlessCredentials.options` to `false`.\
*   If you're using an email, you can configure whether you want the user to receive a magiclink or a OTP.\
*   If you're using phone, you can configure whether you want the user to receive a OTP.\
*   The magic link's destination URL is determined by the [`SITE_URL`](/docs/guides/auth/redirect-urls)\
    .\
*   See [redirect URLs and wildcards](/docs/guides/auth#redirect-urls-and-wildcards)\
     to add additional redirect URLs to your project.\
*   Magic links and OTPs share the same implementation. To send users a one-time code instead of a magic link, [modify the magic link email template](/dashboard/project/_/auth/templates)\
     to include `\{\{ .Token \}\}` instead of `\{\{ .ConfirmationURL \}\}`.\
*   See our [Twilio Phone Auth Guide](/docs/guides/auth/phone-login?showSmsProvider=Twilio)\
     for details about configuring WhatsApp sign in.\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in with emailSign in with SMS OTPSign in with WhatsApp OTP\
\
`     _10  const { data, error } = await supabase.auth.signInWithOtp({  _10  email: 'example@email.com',  _10  options: {  _10  emailRedirectTo: 'https://example.com/welcome'  _10  }  _10  })      `\
\
Response\
\
Notes\
\
* * *\
\
Sign in a user through OAuth\
----------------------------\
\
Log in an existing user via a third-party provider. This method supports the PKCE flow.\
\
*   This method is used for signing in using a third-party provider.\
*   Supabase supports many different [third-party providers](/docs/guides/auth#configure-third-party-providers)\
    .\
\
### Parameters\
\
*   credentialsRequiredSignInWithOAuthCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in using a third-party providerSign in using a third-party provider with redirectSign in with scopes and access provider tokens\
\
`     _10  const { data, error } = await supabase.auth.signInWithOAuth({  _10  provider: 'github'  _10  })      `\
\
Response\
\
* * *\
\
Sign in a user through SSO\
--------------------------\
\
Attempts a single-sign on using an enterprise Identity Provider. A successful SSO attempt will redirect the current page to the identity provider authorization page. The redirect URL is implementation and SSO protocol specific.\
\
*   Before you can call this method you need to [establish a connection](/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections)\
     to an identity provider. Use the [CLI commands](/docs/reference/cli/supabase-sso)\
     to do this.\
*   If you've associated an email domain to the identity provider, you can use the `domain` property to start a sign-in flow.\
*   In case you need to use a different way to start the authentication flow with an identity provider, you can use the `providerId` property. For example:\
    *   Mapping specific user email addresses with an identity provider.\
    *   Using different hints to identity the identity provider to be used by the user, like a company-specific page, IP address or other tracking information.\
\
### Parameters\
\
*   paramsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Sign in with email domainSign in with provider UUID\
\
`     _11  // You can extract the user's email domain and use it to trigger the  _11  // authentication flow with the correct identity provider.  _11  _11  const { data, error } = await supabase.auth.signInWithSSO({  _11  domain: 'company.com'  _11  })  _11  _11  if (data?.url) {  _11  // redirect the user to the identity provider's authentication flow  _11  window.location.href = data.url  _11  }      `\
\
* * *\
\
Sign out a user\
---------------\
\
Inside a browser context, `signOut()` will remove the logged in user from the browser session and log them out - removing all items from localstorage and then trigger a `"SIGNED_OUT"` event.\
\
*   In order to use the `signOut()` method, the user needs to be signed in first.\
*   By default, `signOut()` uses the global scope, which signs out all other sessions that the user is logged into as well.\
*   Since Supabase Auth uses JWTs for authentication, the access token JWT will be valid until it's expired. When the user signs out, Supabase revokes the refresh token and deletes the JWT from the client-side. This does not revoke the JWT and it will still be valid until it expires.\
\
### Parameters\
\
*   optionsRequiredSignOut\
    \
    Details\
    \
\
### Return Type\
\
Promise<object>\
\
Details\
\
Sign out\
\
`     _10  const { error } = await supabase.auth.signOut()      `\
\
* * *\
\
Send a password reset request\
-----------------------------\
\
Sends a password reset request to an email address. This method supports the PKCE flow.\
\
*   The password reset flow consist of 2 broad steps: (i) Allow the user to login via the password reset link; (ii) Update the user's password.\
*   The `resetPasswordForEmail()` only sends a password reset link to the user's email. To update the user's password, see [`updateUser()`](/docs/reference/javascript/auth-updateuser)\
    .\
*   A `SIGNED_IN` and `PASSWORD_RECOVERY` event will be emitted when the password recovery link is clicked. You can use [`onAuthStateChange()`](/docs/reference/javascript/auth-onauthstatechange)\
     to listen and invoke a callback function on these events.\
*   When the user clicks the reset link in the email they are redirected back to your application. You can configure the URL that the user is redirected to with the `redirectTo` parameter. See [redirect URLs and wildcards](/docs/guides/auth#redirect-urls-and-wildcards)\
     to add additional redirect URLs to your project.\
*   After the user has been redirected successfully, prompt them for a new password and call `updateUser()`:\
\
`     _10  const \{ data, error \} = await supabase.auth.updateUser(\{  _10  password: new_password  _10  \})      `\
\
### Parameters\
\
*   emailRequiredstring\
    \
    The email address of the user.\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Reset passwordReset password (React)\
\
`     _10  const { data, error } = await supabase.auth.resetPasswordForEmail(email, {  _10  redirectTo: 'https://example.com/update-password',  _10  })      `\
\
Response\
\
* * *\
\
Verify and log in through OTP\
-----------------------------\
\
Log in a user given a User supplied OTP or TokenHash received through mobile or email.\
\
*   The `verifyOtp` method takes in different verification types. If a phone number is used, the type can either be `sms` or `phone_change`. If an email address is used, the type can be one of the following: `email`, `recovery`, `invite` or `email_change` (`signup` and `magiclink` types are deprecated).\
*   The verification type used should be determined based on the corresponding auth method called before `verifyOtp` to sign up / sign-in a user.\
*   The `TokenHash` is contained in the [email templates](/docs/guides/auth/auth-email-templates)\
     and can be used to sign in. You may wish to use the hash with Magic Links for the PKCE flow for Server Side Auth. See [this guide](/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)\
     for more details.\
\
### Parameters\
\
*   paramsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Verify Signup One-Time Password (OTP)Verify Sms One-Time Password (OTP)Verify Email Auth (Token Hash)\
\
`     _10  const { data, error } = await supabase.auth.verifyOtp({ email, token, type: 'email'})      `\
\
Response\
\
* * *\
\
Retrieve a session\
------------------\
\
Returns the session, refreshing it if necessary.\
\
*   This method retrieves the current local session (i.e local storage).\
*   The session contains a signed JWT and unencoded session data.\
*   Since the unencoded session data is retrieved from the local storage medium, **do not** rely on it as a source of trusted data on the server. It could be tampered with by the sender. If you need verified, trustworthy user data, call [`getUser`](/docs/reference/javascript/auth-getuser)\
     instead.\
*   If the session has an expired access token, this method will use the refresh token to get a new session.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get the session data\
\
`     _10  const { data, error } = await supabase.auth.getSession()      `\
\
Response\
\
* * *\
\
Retrieve a new session\
----------------------\
\
Returns a new session, regardless of expiry status. Takes in an optional current session. If not passed in, then refreshSession() will attempt to retrieve it from getSession(). If the current session's refresh token is invalid, an error will be thrown.\
\
*   This method will refresh and return a new session whether the current one is expired or not.\
\
### Parameters\
\
*   currentSessionOptionalobject\
    \
    The current session. If passed in, it must contain a refresh token.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Refresh session using the current sessionRefresh session using a refresh token\
\
`     _10  const { data, error } = await supabase.auth.refreshSession()  _10  const { session, user } = data      `\
\
Response\
\
* * *\
\
Retrieve a user\
---------------\
\
Gets the current user details if there is an existing session. This method performs a network request to the Supabase Auth server, so the returned value is authentic and can be used to base authorization rules on.\
\
*   This method fetches the user object from the database instead of local session.\
*   This method is useful for checking if the user is authorized because it validates the user's access token JWT on the server.\
*   Should always be used when checking for user authorization on the server. On the client, you can instead use `getSession().session.user` for faster results. `getSession` is insecure on the server.\
\
### Parameters\
\
*   jwtOptionalstring\
    \
    Takes in an optional access token JWT. If no JWT is provided, the JWT from the current session is used.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get the logged in user with the current existing sessionGet the logged in user with a custom access token jwt\
\
`     _10  const { data: { user } } = await supabase.auth.getUser()      `\
\
Response\
\
* * *\
\
Update a user\
-------------\
\
Updates user data for a logged in user.\
\
*   In order to use the `updateUser()` method, the user needs to be signed in first.\
*   By default, email updates sends a confirmation link to both the user's current and new email. To only send a confirmation link to the user's new email, disable **Secure email change** in your project's [email auth provider settings](/dashboard/project/_/auth/providers)\
    .\
\
### Parameters\
\
*   attributesRequiredUserAttributes\
    \
    Details\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Update the email for an authenticated userUpdate the phone number for an authenticated userUpdate the password for an authenticated userUpdate the user's metadataUpdate the user's password with a nonce\
\
`     _10  const { data, error } = await supabase.auth.updateUser({  _10  email: 'new@email.com'  _10  })      `\
\
Response\
\
Notes\
\
* * *\
\
Retrieve identities linked to a user\
------------------------------------\
\
Gets all the identities linked to a user.\
\
*   The user needs to be signed in to call `getUserIdentities()`.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Returns a list of identities linked to the user\
\
`     _10  const { data, error } = await supabase.auth.getUserIdentities()      `\
\
Response\
\
* * *\
\
Link an identity to a user\
--------------------------\
\
Links an oauth identity to an existing user. This method supports the PKCE flow.\
\
*   The **Enable Manual Linking** option must be enabled from your [project's authentication settings](/dashboard/project/_/settings/auth)\
    .\
*   The user needs to be signed in to call `linkIdentity()`.\
*   If the candidate identity is already linked to the existing user or another user, `linkIdentity()` will fail.\
*   If `linkIdentity` is run in the browser, the user is automatically redirected to the returned URL. On the server, you should handle the redirect.\
\
### Parameters\
\
*   credentialsRequiredSignInWithOAuthCredentials\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Link an identity to a user\
\
`     _10  const { data, error } = await supabase.auth.linkIdentity({  _10  provider: 'github'  _10  })      `\
\
Response\
\
* * *\
\
Unlink an identity from a user\
------------------------------\
\
Unlinks an identity from a user by deleting it. The user will no longer be able to sign in with that identity once it's unlinked.\
\
*   The **Enable Manual Linking** option must be enabled from your [project's authentication settings](/dashboard/project/_/settings/auth)\
    .\
*   The user needs to be signed in to call `unlinkIdentity()`.\
*   The user must have at least 2 identities in order to unlink an identity.\
*   The identity to be unlinked must belong to the user.\
\
### Parameters\
\
*   identityRequiredUserIdentity\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Unlink an identity\
\
`     _10  // retrieve all identites linked to a user  _10  const identities = await supabase.auth.getUserIdentities()  _10  _10  // find the google identity  _10  const googleIdentity = identities.find(  _10  identity => identity.provider === 'google'  _10  )  _10  _10  // unlink the google identity  _10  const { error } = await supabase.auth.unlinkIdentity(googleIdentity)      `\
\
* * *\
\
Send a password reauthentication nonce\
--------------------------------------\
\
Sends a reauthentication OTP to the user's email or phone number. Requires the user to be signed-in.\
\
*   This method is used together with `updateUser()` when a user's password needs to be updated.\
*   If you require your user to reauthenticate before updating their password, you need to enable the **Secure password change** option in your [project's email provider settings](/dashboard/project/_/auth/providers)\
    .\
*   A user is only require to reauthenticate before updating their password if **Secure password change** is enabled and the user **hasn't recently signed in**. A user is deemed recently signed in if the session was created in the last 24 hours.\
*   This method will send a nonce to the user's email. If the user doesn't have a confirmed email address, the method will send the nonce to the user's confirmed phone number instead.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Send reauthentication nonce\
\
`     _10  const { error } = await supabase.auth.reauthenticate()      `\
\
Notes\
\
* * *\
\
Resend an OTP\
-------------\
\
Resends an existing signup confirmation email, email change email, SMS OTP or phone change OTP.\
\
*   Resends a signup confirmation, email change or phone change email to the user.\
*   Passwordless sign-ins can be resent by calling the `signInWithOtp()` method again.\
*   Password recovery emails can be resent by calling the `resetPasswordForEmail()` method again.\
*   This method will only resend an email or phone OTP to the user if there was an initial signup, email change or phone change request being made.\
*   You can specify a redirect url when you resend an email link using the `emailRedirectTo` option.\
\
### Parameters\
\
*   credentialsRequiredUnion: expand to see options\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Resend an email signup confirmationResend a phone signup confirmationResend email change emailResend phone change OTP\
\
`     _10  const { error } = await supabase.auth.resend({  _10  type: 'signup',  _10  email: 'email@example.com',  _10  options: {  _10  emailRedirectTo: 'https://example.com/welcome'  _10  }  _10  })      `\
\
Notes\
\
* * *\
\
Set the session data\
--------------------\
\
Sets the session data from the current session. If the current session is expired, setSession will take care of refreshing it to obtain a new session. If the refresh token or access token in the current session is invalid, an error will be thrown.\
\
*   This method sets the session using an `access_token` and `refresh_token`.\
*   If successful, a `SIGNED_IN` event is emitted.\
\
### Parameters\
\
*   currentSessionRequiredobject\
    \
    The current session that minimally contains an access token and refresh token.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Set the session\
\
`     _10  const { data, error } = await supabase.auth.setSession({  _10  access_token,  _10  refresh_token  _10  })      `\
\
Response\
\
Notes\
\
* * *\
\
Exchange an auth code for a session\
-----------------------------------\
\
Log in an existing user by exchanging an Auth Code issued during the PKCE flow.\
\
*   Used when `flowType` is set to `pkce` in client options.\
\
### Parameters\
\
*   authCodeRequiredstring\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Exchange Auth Code\
\
`     _10  supabase.auth.exchangeCodeForSession('34e770dd-9ff9-416c-87fa-43b31d7ef225')      `\
\
Response\
\
* * *\
\
Start auto-refresh session (non-browser)\
----------------------------------------\
\
Starts an auto-refresh process in the background. The session is checked every few seconds. Close to the time of expiration a process is started to refresh the session. If refreshing fails it will be retried for as long as necessary.\
\
*   Only useful in non-browser environments such as React Native or Electron.\
*   The Supabase Auth library automatically starts and stops proactively refreshing the session when a tab is focused or not.\
*   On non-browser platforms, such as mobile or desktop apps built with web technologies, the library is not able to effectively determine whether the application is _focused_ or not.\
*   To give this hint to the application, you should be calling this method when the app is in focus and calling `supabase.auth.stopAutoRefresh()` when it's out of focus.\
\
### Return Type\
\
Promise<void>\
\
Start and stop auto refresh in React Native\
\
`     _10  import { AppState } from 'react-native'  _10  _10  // make sure you register this only once!  _10  AppState.addEventListener('change', (state) => {  _10  if (state === 'active') {  _10  supabase.auth.startAutoRefresh()  _10  } else {  _10  supabase.auth.stopAutoRefresh()  _10  }  _10  })      `\
\
* * *\
\
Stop auto-refresh session (non-browser)\
---------------------------------------\
\
Stops an active auto refresh process running in the background (if any).\
\
*   Only useful in non-browser environments such as React Native or Electron.\
*   The Supabase Auth library automatically starts and stops proactively refreshing the session when a tab is focused or not.\
*   On non-browser platforms, such as mobile or desktop apps built with web technologies, the library is not able to effectively determine whether the application is _focused_ or not.\
*   When your application goes in the background or out of focus, call this method to stop the proactive refreshing of the session.\
\
### Return Type\
\
Promise<void>\
\
Start and stop auto refresh in React Native\
\
`     _10  import { AppState } from 'react-native'  _10  _10  // make sure you register this only once!  _10  AppState.addEventListener('change', (state) => {  _10  if (state === 'active') {  _10  supabase.auth.startAutoRefresh()  _10  } else {  _10  supabase.auth.stopAutoRefresh()  _10  }  _10  })      `\
\
* * *\
\
Auth MFA\
--------\
\
This section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.\
\
Currently, there is support for time-based one-time password (TOTP) and phone verification code as the 2nd factor. Recovery codes are not supported but users can enroll multiple factors, with an upper limit of 10.\
\
Having a 2nd factor for recovery frees the user of the burden of having to store their recovery codes somewhere. It also reduces the attack surface since multiple recovery codes are usually generated compared to just having 1 backup factor.\
\
* * *\
\
Enroll a factor\
---------------\
\
Starts the enrollment process for a new Multi-Factor Authentication (MFA) factor. This method creates a new `unverified` factor. To verify a factor, present the QR code or secret to the user and ask them to add it to their authenticator app. The user has to enter the code from their authenticator app to verify it.\
\
*   Use `totp` or `phone` as the `factorType` and use the returned `id` to create a challenge.\
*   To create a challenge, see [`mfa.challenge()`](/docs/reference/javascript/auth-mfa-challenge)\
    .\
*   To verify a challenge, see [`mfa.verify()`](/docs/reference/javascript/auth-mfa-verify)\
    .\
*   To create and verify a TOTP challenge in a single step, see [`mfa.challengeAndVerify()`](/docs/reference/javascript/auth-mfa-challengeandverify)\
    .\
*   To generate a QR code for the `totp` secret in Next.js, you can do the following:\
\
`     _10  <Image src=\{data.totp.qr_code\} alt=\{data.totp.uri\} layout="fill"></Image>      `\
\
*   The `challenge` and `verify` steps are separated when using Phone factors as the user will need time to receive and input the code obtained from the SMS in challenge.\
\
### Parameters\
\
*   paramsRequiredMFAEnrollParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Enroll a time-based, one-time password (TOTP) factorEnroll a Phone Factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.enroll({  _10  factorType: 'totp',  _10  friendlyName: 'your_friendly_name'  _10  })  _10  _10  // Use the id to create a challenge.  _10  // The challenge can be verified by entering the code generated from the authenticator app.  _10  // The code will be generated upon scanning the qr_code or entering the secret into the authenticator app.  _10  const { id, type, totp: { qr_code, secret, uri }, friendly_name } = data  _10  const challenge = await supabase.auth.mfa.challenge({ factorId: id });      `\
\
Response\
\
* * *\
\
Create a challenge\
------------------\
\
Prepares a challenge used to verify that a user has access to a MFA factor.\
\
*   An [enrolled factor](/docs/reference/javascript/auth-mfa-enroll)\
     is required before creating a challenge.\
*   To verify a challenge, see [`mfa.verify()`](/docs/reference/javascript/auth-mfa-verify)\
    .\
*   A phone factor sends a code to the user upon challenge. The channel defaults to `sms` unless otherwise specified.\
\
### Parameters\
\
*   paramsRequiredMFAChallengeParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create a challenge for a factorCreate a challenge for a phone factorCreate a challenge for a phone factor (WhatsApp)\
\
`     _10  const { data, error } = await supabase.auth.mfa.challenge({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225'  _10  })      `\
\
Response\
\
* * *\
\
Verify a challenge\
------------------\
\
Verifies a code against a challenge. The verification code is provided by the user by entering a code seen in their authenticator app.\
\
*   To verify a challenge, please [create a challenge](/docs/reference/javascript/auth-mfa-challenge)\
     first.\
\
### Parameters\
\
*   paramsRequiredMFAVerifyParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Verify a challenge for a factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.verify({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  challengeId: '4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15',  _10  code: '123456'  _10  })      `\
\
Response\
\
* * *\
\
Create and verify a challenge\
-----------------------------\
\
Helper method which creates a challenge and immediately uses the given code to verify against it thereafter. The verification code is provided by the user by entering a code seen in their authenticator app.\
\
*   Intended for use with only TOTP factors.\
*   An [enrolled factor](/docs/reference/javascript/auth-mfa-enroll)\
     is required before invoking `challengeAndVerify()`.\
*   Executes [`mfa.challenge()`](/docs/reference/javascript/auth-mfa-challenge)\
     and [`mfa.verify()`](/docs/reference/javascript/auth-mfa-verify)\
     in a single step.\
\
### Parameters\
\
*   paramsRequiredMFAChallengeAndVerifyParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create and verify a challenge for a factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.challengeAndVerify({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  code: '123456'  _10  })      `\
\
Response\
\
* * *\
\
Unenroll a factor\
-----------------\
\
Unenroll removes a MFA factor. A user has to have an `aal2` authenticator level in order to unenroll a `verified` factor.\
\
### Parameters\
\
*   paramsRequiredMFAUnenrollParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Unenroll a factor\
\
`     _10  const { data, error } = await supabase.auth.mfa.unenroll({  _10  factorId: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  })      `\
\
Response\
\
* * *\
\
Get Authenticator Assurance Level\
---------------------------------\
\
Returns the Authenticator Assurance Level (AAL) for the active session.\
\
*   Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.\
*   In Supabase, having an AAL of `aal1` refers to having the 1st factor of authentication such as an email and password or OAuth sign-in while `aal2` refers to the 2nd factor of authentication such as a time-based, one-time-password (TOTP) or Phone factor.\
*   If the user has a verified factor, the `nextLevel` field will return `aal2`, else, it will return `aal1`.\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get the AAL details of a session\
\
`     _10  const { data, error } = await supabase.auth.mfa.getAuthenticatorAssuranceLevel()  _10  const { currentLevel, nextLevel, currentAuthenticationMethods } = data      `\
\
Response\
\
* * *\
\
Auth Admin\
----------\
\
*   Any method under the `supabase.auth.admin` namespace requires a `service_role` key.\
*   These methods are considered admin methods and should be called on a trusted server. Never expose your `service_role` key in the browser.\
\
Create server-side auth client\
\
`     _11  import { createClient } from '@supabase/supabase-js'  _11  _11  const supabase = createClient(supabase_url, service_role_key, {  _11  auth: {  _11  autoRefreshToken: false,  _11  persistSession: false  _11  }  _11  })  _11  _11  // Access auth admin api  _11  const adminAuthClient = supabase.auth.admin      `\
\
* * *\
\
Retrieve a user\
---------------\
\
Get user by id.\
\
*   Fetches the user object from the database based on the user's id.\
*   The `getUserById()` method requires the user's id which maps to the `auth.users.id` column.\
\
### Parameters\
\
*   uidRequiredstring\
    \
    The user's unique identifier\
    \
    This function should only be called on a server. Never expose your `service_role` key in the browser.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Fetch the user object using the access\_token jwt\
\
`     _10  const { data, error } = await supabase.auth.admin.getUserById(1)      `\
\
Response\
\
* * *\
\
List all users\
--------------\
\
Get a list of users.\
\
*   Defaults to return 50 users per page.\
\
### Parameters\
\
*   paramsOptionalPageParams\
    \
    An object which supports `page` and `perPage` as numbers, to alter the paginated results.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get a page of usersPaginated list of users\
\
`     _10  const { data: { users }, error } = await supabase.auth.admin.listUsers()      `\
\
* * *\
\
Create a user\
-------------\
\
Creates a new user. This function should only be called on a server. Never expose your `service_role` key in the browser.\
\
*   To confirm the user's email address or phone number, set `email_confirm` or `phone_confirm` to true. Both arguments default to false.\
*   `createUser()` will not send a confirmation email to the user. You can use [`inviteUserByEmail()`](/docs/reference/javascript/auth-admin-inviteuserbyemail)\
     if you want to send them an email invite instead.\
*   If you are sure that the created user's email or phone number is legitimate and verified, you can set the `email_confirm` or `phone_confirm` param to `true`.\
\
### Parameters\
\
*   attributesRequiredAdminUserAttributes\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
With custom user metadataAuto-confirm the user's emailAuto-confirm the user's phone number\
\
`     _10  const { data, error } = await supabase.auth.admin.createUser({  _10  email: 'user@email.com',  _10  password: 'password',  _10  user_metadata: { name: 'Yoda' }  _10  })      `\
\
Response\
\
* * *\
\
Delete a user\
-------------\
\
Delete a user. Requires a `service_role` key.\
\
*   The `deleteUser()` method requires the user's ID, which maps to the `auth.users.id` column.\
\
### Parameters\
\
*   idRequiredstring\
    \
    The user id you want to remove.\
    \
*   shouldSoftDeleteRequiredboolean\
    \
    If true, then the user will be soft-deleted (setting `deleted_at` to the current timestamp and disabling their account while preserving their data) from the auth schema. Defaults to false for backward compatibility.\
    \
    This function should only be called on a server. Never expose your `service_role` key in the browser.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Removes a user\
\
`     _10  const { data, error } = await supabase.auth.admin.deleteUser(  _10  '715ed5db-f090-4b8c-a067-640ecee36aa0'  _10  )      `\
\
Response\
\
* * *\
\
Send an email invite link\
-------------------------\
\
Sends an invite link to an email address.\
\
*   Sends an invite link to the user's email address.\
*   The `inviteUserByEmail()` method is typically used by administrators to invite users to join the application.\
*   Note that PKCE is not supported when using `inviteUserByEmail`. This is because the browser initiating the invite is often different from the browser accepting the invite which makes it difficult to provide the security guarantees required of the PKCE flow.\
\
### Parameters\
\
*   emailRequiredstring\
    \
    The email address of the user.\
    \
*   optionsRequiredobject\
    \
    Additional options to be included when inviting.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Invite a user\
\
`     _10  const { data, error } = await supabase.auth.admin.inviteUserByEmail('email@example.com')      `\
\
Response\
\
* * *\
\
Generate an email link\
----------------------\
\
Generates email links and OTPs to be sent via a custom email provider.\
\
*   The following types can be passed into `generateLink()`: `signup`, `magiclink`, `invite`, `recovery`, `email_change_current`, `email_change_new`, `phone_change`.\
*   `generateLink()` only generates the email link for `email_change_email` if the **Secure email change** is enabled in your project's [email auth provider settings](/dashboard/project/_/auth/providers)\
    .\
*   `generateLink()` handles the creation of the user for `signup`, `invite` and `magiclink`.\
\
### Parameters\
\
*   paramsRequiredGenerateLinkParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Generate a signup linkGenerate an invite linkGenerate a magic linkGenerate a recovery linkGenerate links to change current email address\
\
`     _10  const { data, error } = await supabase.auth.admin.generateLink({  _10  type: 'signup',  _10  email: 'email@example.com',  _10  password: 'secret'  _10  })      `\
\
Response\
\
* * *\
\
Update a user\
-------------\
\
Updates the user data.\
\
### Parameters\
\
*   uidRequiredstring\
    \
*   attributesRequiredAdminUserAttributes\
    \
    The data you want to update.\
    \
    This function should only be called on a server. Never expose your `service_role` key in the browser.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Updates a user's emailUpdates a user's passwordUpdates a user's metadataUpdates a user's app\_metadataConfirms a user's email addressConfirms a user's phone number\
\
`     _10  const { data: user, error } = await supabase.auth.admin.updateUserById(  _10  '11111111-1111-1111-1111-111111111111',  _10  { email: 'new@email.com' }  _10  )      `\
\
Response\
\
* * *\
\
Delete a factor for a user\
--------------------------\
\
Deletes a factor on a user. This will log the user out of all active sessions if the deleted factor was verified.\
\
### Parameters\
\
*   paramsRequiredAuthMFAAdminDeleteFactorParams\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Delete a factor for a user\
\
`     _10  const { data, error } = await supabase.auth.admin.mfa.deleteFactor({  _10  id: '34e770dd-9ff9-416c-87fa-43b31d7ef225',  _10  userId: 'a89baba7-b1b7-440f-b4bb-91026967f66b',  _10  })      `\
\
Response\
\
* * *\
\
Invokes a Supabase Edge Function.\
---------------------------------\
\
Invokes a function\
\
Invoke a Supabase Edge Function.\
\
*   Requires an Authorization header.\
*   Invoke params generally match the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)\
     spec.\
*   When you pass in a body to your function, we automatically attach the Content-Type header for `Blob`, `ArrayBuffer`, `File`, `FormData` and `String`. If it doesn't match any of these types we assume the payload is `json`, serialize it and attach the `Content-Type` header as `application/json`. You can override this behavior by passing in a `Content-Type` header of your own.\
*   Responses are automatically parsed as `json`, `blob` and `form-data` depending on the `Content-Type` header sent by your function. Responses are parsed as `text` by default.\
\
### Parameters\
\
*   functionNameRequiredstring\
    \
    The name of the Function to invoke.\
    \
*   optionsRequiredFunctionInvokeOptions\
    \
    Options for invoking the Function.\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Basic invocationError handlingPassing custom headersCalling with DELETE HTTP verbInvoking a Function in the UsEast1 regionCalling with GET HTTP verb\
\
`     _10  const { data, error } = await supabase.functions.invoke('hello', {  _10  body: { foo: 'bar' }  _10  })      `\
\
* * *\
\
Subscribe to channel\
--------------------\
\
Creates an event handler that listens to changes.\
\
*   By default, Broadcast and Presence are enabled for all projects.\
*   By default, listening to database changes is disabled for new projects due to database performance and security concerns. You can turn it on by managing Realtime's [replication](/docs/guides/api#realtime-api-overview)\
    .\
*   You can receive the "previous" data for updates and deletes by setting the table's `REPLICA IDENTITY` to `FULL` (e.g., `ALTER TABLE your_table REPLICA IDENTITY FULL;`).\
*   Row level security is not applied to delete statements. When RLS is enabled and replica identity is set to full, only the primary key is sent to clients.\
\
### Parameters\
\
*   typeRequiredUnion: expand to see options\
    \
    Details\
    \
*   filterRequiredUnion: expand to see options\
    \
    Details\
    \
*   callbackRequiredfunction\
    \
    Details\
    \
\
Listen to broadcast messagesListen to presence syncListen to presence joinListen to presence leaveListen to all database changesListen to a specific tableListen to insertsListen to updatesListen to deletesListen to multiple eventsListen to row level changes\
\
`     _13  const channel = supabase.channel("room1")  _13  _13  channel.on("broadcast", { event: "cursor-pos" }, (payload) => {  _13  console.log("Cursor position received!", payload);  _13  }).subscribe((status) => {  _13  if (status === "SUBSCRIBED") {  _13  channel.send({  _13  type: "broadcast",  _13  event: "cursor-pos",  _13  payload: { x: Math.random(), y: Math.random() },  _13  });  _13  }  _13  });      `\
\
* * *\
\
Unsubscribe from a channel\
--------------------------\
\
Unsubscribes and removes Realtime channel from Realtime client.\
\
*   Removing a channel is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.\
\
### Parameters\
\
*   channelRequired@supabase/realtime-js.RealtimeChannel\
    \
    The name of the Realtime channel.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Removes a channel\
\
`     _10  supabase.removeChannel(myChannel)      `\
\
* * *\
\
Unsubscribe from all channels\
-----------------------------\
\
Unsubscribes and removes all Realtime channels from Realtime client.\
\
*   Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.\
\
### Return Type\
\
Promise<Array<Union: expand to see options>>\
\
Details\
\
Remove all channels\
\
`     _10  supabase.removeAllChannels()      `\
\
* * *\
\
Retrieve all channels\
---------------------\
\
Returns all Realtime channels.\
\
### Return Type\
\
Array<@supabase/realtime-js.RealtimeChannel>\
\
Get all channels\
\
`     _10  const channels = supabase.getChannels()      `\
\
* * *\
\
Broadcast a message\
-------------------\
\
Sends a message into the channel.\
\
Broadcast a message to all connected clients to a channel.\
\
*   When using REST you don't need to subscribe to the channel\
*   REST calls are only available from 2.37.0 onwards\
\
### Parameters\
\
*   argsRequiredobject\
    \
    Arguments to send to channel\
    \
    Details\
    \
*   optsRequired{ \[key: string\]: any }\
    \
    Options to be used during the send process\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Send a message via websocketSend a message via REST\
\
`     _11  supabase  _11  .channel('room1')  _11  .subscribe((status) => {  _11  if (status === 'SUBSCRIBED') {  _11  channel.send({  _11  type: 'broadcast',  _11  event: 'cursor-pos',  _11  payload: { x: Math.random(), y: Math.random() },  _11  })  _11  }  _11  })      `\
\
Response\
\
* * *\
\
Create a bucket\
---------------\
\
Creates a new Storage bucket\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `insert`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    A unique identifier for the bucket you are creating.\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .createBucket('avatars', {  _10  public: false,  _10  allowedMimeTypes: ['image/png'],  _10  fileSizeLimit: 1024  _10  })      `\
\
Response\
\
* * *\
\
Retrieve a bucket\
-----------------\
\
Retrieves the details of an existing Storage bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    The unique identifier of the bucket you would like to retrieve.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Get bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .getBucket('avatars')      `\
\
Response\
\
* * *\
\
List all buckets\
----------------\
\
Retrieves the details of all Storage buckets within an existing project.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
List buckets\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .listBuckets()      `\
\
Response\
\
* * *\
\
Update a bucket\
---------------\
\
Updates a Storage bucket\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select` and `update`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    A unique identifier for the bucket you are updating.\
    \
*   optionsRequiredobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Update bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .updateBucket('avatars', {  _10  public: false,  _10  allowedMimeTypes: ['image/png'],  _10  fileSizeLimit: 1024  _10  })      `\
\
Response\
\
* * *\
\
Delete a bucket\
---------------\
\
Deletes an existing bucket. A bucket can't be deleted with existing objects inside it. You must first `empty()` the bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select` and `delete`\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    The unique identifier of the bucket you would like to delete.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Delete bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .deleteBucket('avatars')      `\
\
Response\
\
* * *\
\
Empty a bucket\
--------------\
\
Removes all objects inside a single bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: `select`\
    *   `objects` table permissions: `select` and `delete`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   idRequiredstring\
    \
    The unique identifier of the bucket you would like to empty.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Empty bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .emptyBucket('avatars')      `\
\
Response\
\
* * *\
\
Upload a file\
-------------\
\
Uploads a file to an existing bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: only `insert` when you are uploading new files and `select`, `insert` and `update` when you are upserting files\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
*   For React Native, using either `Blob`, `File` or `FormData` does not work as intended. Upload file using `ArrayBuffer` from base64 file data instead, see example below.\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.\
    \
*   fileBodyRequiredFileBody\
    \
    The body of the file to be stored in the bucket.\
    \
*   fileOptionsOptionalFileOptions\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Upload fileUpload file using \`ArrayBuffer\` from base64 file data\
\
`     _10  const avatarFile = event.target.files[0]  _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .upload('public/avatar1.png', avatarFile, {  _10  cacheControl: '3600',  _10  upsert: false  _10  })      `\
\
Response\
\
* * *\
\
Download a file\
---------------\
\
Downloads a file from a private bucket. For public buckets, make a request to the URL returned from `getPublicUrl` instead.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The full path and file name of the file to be downloaded. For example `folder/image.png`.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Download fileDownload file with transformations\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .download('folder/avatar1.png')      `\
\
Response\
\
* * *\
\
List all files in a bucket\
--------------------------\
\
Lists all the files within a bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathOptionalstring\
    \
    The folder path.\
    \
*   optionsOptionalSearchOptions\
    \
    Details\
    \
*   parametersOptionalFetchParameters\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
List files in a bucketSearch files in a bucket\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .list('folder', {  _10  limit: 100,  _10  offset: 0,  _10  sortBy: { column: 'name', order: 'asc' },  _10  })      `\
\
Response\
\
* * *\
\
Replace an existing file\
------------------------\
\
Replaces an existing file at the specified path with a new one.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `update` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
*   For React Native, using either `Blob`, `File` or `FormData` does not work as intended. Update file using `ArrayBuffer` from base64 file data instead, see example below.\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The relative file path. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to update.\
    \
*   fileBodyRequiredUnion: expand to see options\
    \
    The body of the file to be stored in the bucket.\
    \
    Details\
    \
*   fileOptionsOptionalFileOptions\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Update fileUpdate file using \`ArrayBuffer\` from base64 file data\
\
`     _10  const avatarFile = event.target.files[0]  _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .update('public/avatar1.png', avatarFile, {  _10  cacheControl: '3600',  _10  upsert: true  _10  })      `\
\
Response\
\
* * *\
\
Move an existing file\
---------------------\
\
Moves an existing file to a new path in the same bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `update` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   fromPathRequiredstring\
    \
    The original file path, including the current file name. For example `folder/image.png`.\
    \
*   toPathRequiredstring\
    \
    The new file path, including the new file name. For example `folder/image-new.png`.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Move file\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .move('public/avatar1.png', 'private/avatar2.png')      `\
\
Response\
\
* * *\
\
Copy an existing file\
---------------------\
\
Copies an existing file to a new path in the same bucket.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `insert` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   fromPathRequiredstring\
    \
    The original file path, including the current file name. For example `folder/image.png`.\
    \
*   toPathRequiredstring\
    \
    The new file path, including the new file name. For example `folder/image-copy.png`.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Copy file\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .copy('public/avatar1.png', 'private/avatar2.png')      `\
\
Response\
\
* * *\
\
Delete files in a bucket\
------------------------\
\
Deletes files within the same bucket\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `delete` and `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathsRequiredArray<string>\
    \
    An array of files to delete, including the path and file name. For example \[`'folder/image.png'`\].\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Delete file\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .remove(['folder/avatar1.png'])      `\
\
Response\
\
* * *\
\
Create a signed URL\
-------------------\
\
Creates a signed URL. Use a signed URL to share a file for a fixed amount of time.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the current file name. For example `folder/image.png`.\
    \
*   expiresInRequirednumber\
    \
    The number of seconds until the signed URL expires. For example, `60` for a URL which is valid for one minute.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create Signed URLCreate a signed URL for an asset with transformationsCreate a signed URL which triggers the download of the asset\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .createSignedUrl('folder/avatar1.png', 60)      `\
\
Response\
\
* * *\
\
Create signed URLs\
------------------\
\
Creates multiple signed URLs. Use a signed URL to share a file for a fixed amount of time.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `select`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathsRequiredArray<string>\
    \
    The file paths to be downloaded, including the current file names. For example `['folder/image.png', 'folder2/image2.png']`.\
    \
*   expiresInRequirednumber\
    \
    The number of seconds until the signed URLs expire. For example, `60` for URLs which are valid for one minute.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create Signed URLs\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .createSignedUrls(['folder/avatar1.png', 'folder/avatar2.png'], 60)      `\
\
Response\
\
* * *\
\
Create signed upload URL\
------------------------\
\
Creates a signed upload URL. Signed upload URLs can be used to upload files to the bucket without further authentication. They are valid for 2 hours.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: `insert`\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the current file name. For example `folder/image.png`.\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Create Signed Upload URL\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .createSignedUploadUrl('folder/cat.jpg')      `\
\
Response\
\
* * *\
\
Upload to a signed URL\
----------------------\
\
Upload a file with a token generated from `createSignedUploadUrl`.\
\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.\
    \
*   tokenRequiredstring\
    \
    The token generated from `createSignedUploadUrl`\
    \
*   fileBodyRequiredFileBody\
    \
    The body of the file to be stored in the bucket.\
    \
*   fileOptionsOptionalFileOptions\
    \
    Details\
    \
\
### Return Type\
\
Promise<Union: expand to see options>\
\
Details\
\
Upload to a signed URL\
\
`     _10  const { data, error } = await supabase  _10  .storage  _10  .from('avatars')  _10  .uploadToSignedUrl('folder/cat.jpg', 'token-from-createSignedUploadUrl', file)      `\
\
Response\
\
* * *\
\
Retrieve public URL\
-------------------\
\
A simple convenience function to get the URL for an asset in a public bucket. If you do not want to use this function, you can construct the public URL by concatenating the bucket URL with the path to the asset. This function does not verify if the bucket is public. If a public URL is created for a bucket which is not public, you will not be able to download the asset.\
\
*   The bucket needs to be set to public, either via [updateBucket()](/docs/reference/javascript/storage-updatebucket)\
     or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard)\
    , clicking the overflow menu on a bucket and choosing "Make public"\
*   RLS policy permissions required:\
    *   `buckets` table permissions: none\
    *   `objects` table permissions: none\
*   Refer to the [Storage guide](/docs/guides/storage/security/access-control)\
     on how access control works\
\
### Parameters\
\
*   pathRequiredstring\
    \
    The path and name of the file to generate the public URL for. For example `folder/image.png`.\
    \
*   optionsOptionalobject\
    \
    Details\
    \
\
### Return Type\
\
object\
\
Details\
\
Returns the URL for an asset in a public bucketReturns the URL for an asset in a public bucket with transformationsReturns the URL which triggers the download of an asset in a public bucket\
\
`     _10  const { data } = supabase  _10  .storage  _10  .from('public-bucket')  _10  .getPublicUrl('folder/avatar1.png')      `\
\
Response\
\
* * *\
\
Release Notes\
-------------\
\
Supabase.js v2 release notes.\
\
Install the latest version of @supabase/supabase-js\
\
Terminal\
\
`     _10  npm install @supabase/supabase-js      `\
\
### Explicit constructor options[#](#explicit-constructor-options)\
\
All client specific options within the constructor are keyed to the library.\
\
See [PR](https://github.com/supabase/supabase-js/pull/458)\
:\
\
`     _19  const supabase = createClient(apiURL, apiKey, {  _19  db: {  _19  schema: 'public',  _19  },  _19  auth: {  _19  storage: AsyncStorage,  _19  autoRefreshToken: true,  _19  persistSession: true,  _19  detectSessionInUrl: true,  _19  },  _19  realtime: {  _19  channels,  _19  endpoint,  _19  },  _19  global: {  _19  fetch: customFetch,  _19  headers: DEFAULT_HEADERS,  _19  },  _19  })      `\
\
### TypeScript support[#](#typescript-support)\
\
The libraries now support typescript.\
\
v1.0\
\
``     _10  // previously definitions were injected in the `from()` method  _10  supabase.from<Definitions['Message']>('messages').select('\*')      ``\
\
* * *\
\
v2.0\
\
``     _10  import type { Database } from './DatabaseDefinitions'  _10  _10  // definitions are injected in `createClient()`  _10  const supabase = createClient<Database>(SUPABASE_URL, ANON_KEY)  _10  _10  const { data } = await supabase.from('messages').select().match({ id: 1 })      ``\
\
Types can be generated via the CLI:\
\
Terminal\
\
`     _10  supabase start  _10  supabase gen types typescript --local > DatabaseDefinitions.ts      `\
\
### Data operations return minimal[#](#data-operations-return-minimal)\
\
`.insert()` / `.upsert()` / `.update()` / `.delete()` don't return rows by default: [PR](https://github.com/supabase/postgrest-js/pull/276)\
.\
\
Previously, these methods return inserted/updated/deleted rows by default (which caused [some confusion](https://github.com/supabase/supabase/discussions/1548)\
), and you can opt to not return it by specifying `returning: 'minimal'`. Now the default behavior is to not return rows. To return inserted/updated/deleted rows, add a `.select()` call at the end, e.g.:\
\
`     _10  const { data, error } = await supabase  _10  .from('my_table')  _10  .delete()  _10  .eq('id', 1)  _10  .select()      `\
\
### New ordering defaults[#](#new-ordering-defaults)\
\
`.order()` now defaults to Postgres’s default: [PR](https://github.com/supabase/postgrest-js/pull/283)\
.\
\
Previously `nullsFirst` defaults to `false` , meaning `null`s are ordered last. This is bad for performance if e.g. the column uses an index with `NULLS FIRST` (which is the default direction for indexes).\
\
### Cookies and localstorage namespace[#](#cookies-and-localstorage-namespace)\
\
Storage key name in the Auth library has changed to include project reference which means that existing websites that had their JWT expiry set to a longer time could find their users logged out with this upgrade.\
\
``     _10  const defaultStorageKey = `sb-${new URL(this.authUrl).hostname.split('.')[0]}-auth-token`      ``\
\
### New Auth Types[#](#new-auth-types)\
\
Typescript typings have been reworked. `Session` interface now guarantees that it will always have an `access_token`, `refresh_token` and `user`\
\
./types.ts\
\
`     _10  interface Session {  _10  provider_token?: string | null  _10  access_token: string  _10  expires_in?: number  _10  expires_at?: number  _10  refresh_token: string  _10  token_type: string  _10  user: User  _10  }      `\
\
### New Auth methods[#](#new-auth-methods)\
\
We're removing the `signIn()` method in favor of more explicit function signatures: `signInWithPassword()`, `signInWithOtp()`, and `signInWithOAuth()`.\
\
v1.0\
\
`     _10  const { data } = await supabase.auth.signIn({  _10  email: 'hello@example',  _10  password: 'pass',  _10  })      `\
\
* * *\
\
v2.0\
\
`     _10  const { data } = await supabase.auth.signInWithPassword({  _10  email: 'hello@example',  _10  password: 'pass',  _10  })      `\
\
### New Realtime methods[#](#new-realtime-methods)\
\
There is a new `channel()` method in the Realtime library, which will be used for our Multiplayer updates.\
\
We will deprecate the `.from().on().subscribe()` method previously used for listening to postgres changes.\
\
`     _21  supabase  _21  .channel('any_string_you_want')  _21  .on('presence', { event: 'track' }, (payload) => {  _21  console.log(payload)  _21  })  _21  .subscribe()  _21  _21  supabase  _21  .channel('any_string_you_want')  _21  .on(  _21  'postgres_changes',  _21  {  _21  event: 'INSERT',  _21  schema: 'public',  _21  table: 'movies',  _21  },  _21  (payload) => {  _21  console.log(payload)  _21  }  _21  )  _21  .subscribe()      `\
\
### Deprecated setAuth()[#](#deprecated-setauth)\
\
Deprecated and removed `setAuth()` . To set a custom `access_token` jwt instead, pass the custom header into the `createClient()` method provided: ([PR](https://github.com/supabase/gotrue-js/pull/340)\
)\
\
### All changes[#](#all-changes)\
\
*   `supabase-js`\
    *   `shouldThrowOnError` has been removed until all the client libraries support this option ([PR](https://github.com/supabase/supabase-js/pull/490)\
        ).\
*   `postgrest-js`\
    *   TypeScript typings have been reworked [PR](https://github.com/supabase/postgrest-js/pull/279)\
        \
    *   Use `undefined` instead of `null` for function params, types, etc. ([https://github.com/supabase/postgrest-js/pull/278](https://github.com/supabase/postgrest-js/pull/278)\
        )\
    *   Some features are now obsolete: ([https://github.com/supabase/postgrest-js/pull/275](https://github.com/supabase/postgrest-js/pull/275)\
        )\
        *   filter shorthands (e.g. `cs` vs. `contains`)\
        *   `body` in response (vs. `data`)\
        *   `upsert`ing through the `.insert()` method\
        *   `auth` method on `PostgrestClient`\
        *   client-level `throwOnError`\
*   `gotrue-js`\
    *   `supabase-js` client allows passing a `storageKey` param which will allow the user to set the key used in local storage for storing the session. By default, this will be namespace-d with the supabase project ref. ([PR](https://github.com/supabase/supabase-js/pull/460)\
        )\
    *   `signIn` method is now split into `signInWithPassword` , `signInWithOtp` , `signInWithOAuth` ([PR](https://github.com/supabase/gotrue-js/pull/304)\
        )\
    *   Deprecated and removed `session()` , `user()` in favour of using `getSession()` instead. `getSession()` will always return a valid session if a user is already logged in, meaning no more random logouts. ([PR](https://github.com/supabase/gotrue-js/pull/299)\
        )\
    *   Deprecated and removed setting for `multitab` support because `getSession()` and gotrue’s reuse interval setting takes care of session management across multiple tabs ([PR](https://github.com/supabase/gotrue-js/pull/366)\
        )\
    *   No more throwing of random errors, gotrue-js v2 always returns a custom error type: ([PR](https://github.com/supabase/gotrue-js/pull/341)\
        )\
        *   `AuthSessionMissingError`\
            *   Indicates that a session is expected but missing\
        *   `AuthNoCookieError`\
            *   Indicates that a cookie is expected but missing\
        *   `AuthInvalidCredentialsError`\
            *   Indicates that the incorrect credentials were passed\
    *   Renamed the `api` namespace to `admin` , the `admin` namespace will only contain methods that should only be used in a trusted server-side environment with the service role key\
    *   Moved `resetPasswordForEmail` , `getUser` and `updateUser` to the `GoTrueClient` which means they will be accessible from the `supabase.auth` namespace in `supabase-js` instead of having to do `supabase.auth.api` to access them\
    *   Removed `sendMobileOTP` , `sendMagicLinkEmail` in favor of `signInWithOtp`\
    *   Removed `signInWithEmail`, `signInWithPhone` in favor of `signInWithPassword`\
    *   Removed `signUpWithEmail` , `signUpWithPhone` in favor of `signUp`\
    *   Replaced `update` with `updateUser`\
*   `storage-js`\
    *   Return types are more strict. Functions types used to indicate that the data returned could be null even if there was no error. We now make use of union types which only mark the data as null if there is an error and vice versa. ([PR](https://github.com/supabase/storage-js/pull/60)\
        )\
    *   The `upload` and `update` function returns the path of the object uploaded as the `path` parameter. Previously the returned value had the bucket name prepended to the path which made it harder to pass the value on to other storage-js methods since all methods take the bucket name and path separately. We also chose to call the returned value `path` instead of `Key` ([PR](https://github.com/supabase/storage-js/pull/75)\
        )\
    *   `getPublicURL` only returns the public URL inside the data object. This keeps it consistent with our other methods of returning only within the data object. No error is returned since this method cannot does not throw an error ([PR](https://github.com/supabase/storage-js/pull/93)\
        )\
    *   signed urls are returned as `signedUrl` instead of `signedURL` in both `createSignedUrl` and `createSignedUrls` ([PR](https://github.com/supabase/storage-js/pull/94)\
        )\
    *   Encodes URLs returned by `createSignedUrl`, `createSignedUrls` and `getPublicUrl` ([PR](https://github.com/supabase/storage-js/pull/86)\
        )\
    *   `createsignedUrl` used to return a url directly and and within the data object. This was inconsistent. Now we always return values only inside the data object across all methods. ([PR](https://github.com/supabase/storage-js/pull/88)\
        )\
    *   `createBucket` returns a data object instead of the name of the bucket directly. ([PR](https://github.com/supabase/storage-js/pull/89)\
        )\
    *   Fixed types for metadata ([PR](https://github.com/supabase/storage-js/pull/90)\
        )\
    *   Better error types make it easier to track down what went wrong quicker.\
    *   `SupabaseStorageClient` is no longer exported. Use `StorageClient` instead. ([PR](https://github.com/supabase/storage-js/pull/92)\
        ).\
*   `realtime-js`\
    *   `RealtimeSubscription` class no longer exists and replaced by `RealtimeChannel`.\
    *   `RealtimeClient`'s `disconnect` method now returns type of `void` . It used to return type of `Promise<{ error: Error | null; data: boolean }`.\
    *   Removed `removeAllSubscriptions` and `removeSubscription` methods from `SupabaseClient` class.\
    *   Removed `SupabaseRealtimeClient` class.\
    *   Removed `SupabaseQueryBuilder` class.\
    *   Removed `SupabaseEventTypes` type.\
        *   Thinking about renaming this to something like `RealtimePostgresChangeEvents` and moving it to `realtime-js` v2.\
    *   Removed `.from(’table’).on(’INSERT’, () ⇒ {}).subscribe()` in favor of new Realtime client API.\
*   `functions-js`\
    *   supabase-js v1 only threw an error if the fetch call itself threw an error (network errors, etc) and not if the function returned HTTP errors like 400s or 500s. We have changed this behaviour to return an error if your function throws an error.\
    *   We have introduced new error types to distinguish between different kinds of errors. A `FunctionsHttpError` error is returned if your function throws an error, `FunctionsRelayError` if the Supabase Relay has an error processing your function and `FunctionsFetchError` if there is a network error in calling your function.\
    *   The correct content-type headers are automatically attached when sending the request if you don’t pass in a `Content-Type` header and pass in an argument to your function. We automatically attach the content type for `Blob`, `ArrayBuffer`, `File`, `FormData` ,`String` . If it doesn’t match any of these we assume the payload is `json` , we serialise the payload as JSON and attach the content type as `application/json`.\
    *   `responseType` does not need to be explicitly passed in. We parse the response based on the `Content-Type` response header sent by the function. We support parsing the responses as `text`, `json`, `blob`, `form-data` and are parsed as `text` by default.\
\
*   Need some help?\
    \
    [Contact support](https://supabase.com/support)\
    \
*   Latest product updates?\
    \
    [See Changelog](https://supabase.com/changelog)\
    \
*   Something's not right?\
    \
    [Check system status](https://status.supabase.com/)\
    \
\
* * *\
\
[© Supabase Inc](https://supabase.com/)\
—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)\
[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)\
[Open Source](https://supabase.com/open-source)\
[SupaSquad](https://supabase.com/supasquad)\
Privacy Settings\
\
[GitHub](https://github.com/supabase/supabase)\
[Twitter](https://twitter.com/supabase)\
[Discord](https://discord.supabase.com/)