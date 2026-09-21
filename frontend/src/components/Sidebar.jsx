function Sidebar() {
  return (
    <div className="w-64 bg-blue-700 text-white p-5">

      <h1 className="text-2xl font-bold">
        BP Poddar AI
      </h1>

      <p className="text-sm mt-2 text-blue-100">
        Your College Assistant
      </p>

      <div className="mt-8 space-y-3">

        <button className="w-full text-left bg-blue-600 p-3 rounded-lg">
          Semester
        </button>

        <button className="w-full text-left bg-blue-600 p-3 rounded-lg">
          Departments
        </button>

        <button className="w-full text-left bg-blue-600 p-3 rounded-lg">
          PYQs
        </button>

        <button className="w-full text-left bg-blue-600 p-3 rounded-lg">
          Faculty
        </button>

      </div>

    </div>
  );
}

export default Sidebar;